# -*- coding: utf-8 -*-

!pip install -q pypdf sentence-transformers chromadb transformers accelerate
print("✅ Installation complete")


from google.colab import files

uploaded_files = files.upload()

print(f"✅ Uploaded {len(uploaded_files)} file(s)")
for filename in uploaded_files:
    print(" -", filename)

!pip install -q pypdf
from pypdf import PdfReader

documents = []

for filename in uploaded_files:
    reader = PdfReader(filename)

    for page_number, page in enumerate(reader.pages, start=1):
        text = page.extract_text()

        if text and text.strip():
            documents.append({
                "text": text.strip(),
                "source": filename,
                "page": page_number
            })

print("✅ Text extraction complete")
print("Pages extracted:", len(documents))

for doc in documents[:2]:
    print("\nSOURCE:", doc["source"])
    print("PAGE:", doc["page"])
    print("TEXT PREVIEW:", doc["text"][:500])


CHUNK_SIZE = 500
CHUNK_OVERLAP = 50

chunks = []
chunk_id = 0

for document in documents:
    words = document["text"].split()
    start = 0

    while start < len(words):
        end = start + CHUNK_SIZE
        chunk_text = " ".join(words[start:end])

        if chunk_text.strip():
            chunks.append({
                "chunk_id": chunk_id,
                "text": chunk_text,
                "source": document["source"],
                "page": document["page"]
            })
            chunk_id += 1

        start += CHUNK_SIZE - CHUNK_OVERLAP

print("✅ Chunking complete")
print("Total chunks:", len(chunks))

for chunk in chunks[:3]:
    print("=" * 60)
    print("CHUNK:", chunk["chunk_id"])
    print("SOURCE:", chunk["source"])
    print("PAGE:", chunk["page"])
    print("TEXT:", chunk["text"][:400])


from sentence_transformers import SentenceTransformer

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")

texts = [chunk["text"] for chunk in chunks]

embeddings = embedding_model.encode(
    texts,
    show_progress_bar=True
)

print("✅ Embeddings created")
print("Number of vectors:", len(embeddings))
print("Vector dimensions:", len(embeddings[0]))

!pip install -q chromadb
import chromadb

chroma_client = chromadb.Client()

collection = chroma_client.get_or_create_collection(
    name="to_do_knowledge"
)

collection.add(
    ids=[str(chunk["chunk_id"]) for chunk in chunks],
    documents=texts,
    embeddings=embeddings.tolist(),
    metadatas=[
        {
            "source": chunk["source"],
            "page": chunk["page"]
        }
        for chunk in chunks
    ]
)

print("✅ Vector database ready")
print("Stored chunks:", collection.count())


question = input("Ask a day plan query : ")

query_embedding = embedding_model.encode(
    [question]
)[0].tolist()

print("\nQUESTION:", question)
print("✅ Query embedding created")


results = collection.query(
    query_embeddings=[query_embedding],
    n_results=min(3, len(chunks))
)

print("✅ Similarity search complete")

retrieved_chunks = []

for i, text in enumerate(results["documents"][0]):
    metadata = results["metadatas"][0][i]
    distance = results["distances"][0][i]

    item = {
        "text": text,
        "source": metadata["source"],
        "page": metadata["page"],
        "distance": distance
    }

    retrieved_chunks.append(item)

    print("=" * 60)
    print("RANK:", i + 1)
    print("DISTANCE:", round(distance, 4))
    print("SOURCE:", metadata["source"])
    print("PAGE:", metadata["page"])
    print("TEXT:", text[:700])


context = "\n\n".join(
    f"SOURCE: {chunk['source']}\n"
    f"PAGE: {chunk['page']}\n"
    f"CONTENT: {chunk['text']}"
    for chunk in retrieved_chunks
)

prompt = (
    "You are a productivity agent.\n\n"
    "Answer the question using ONLY the productivity policy context below. "
    "Do not invent policies.\n\n"
    "QUESTION:\n" + question + "\n\n"
    "productivity POLICY CONTEXT:\n" + context
)

print("✅ RAG prompt created")
print(prompt[:3500])


import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"

device = "cuda" if torch.cuda.is_available() else "cpu"

print("Loading local LLM on:", device)

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
)

model = model.to(device)
model.eval()

print("✅ Local LLM loaded")

if 'tokenizer' not in globals() or 'model' not in globals():
    import torch
    from transformers import AutoTokenizer, AutoModelForCausalLM

    MODEL_NAME = "Qwen/Qwen2.5-0.5B-Instruct"
    device = "cuda" if torch.cuda.is_available() else "cpu"

    print("Re-loading local LLM components due to NameError...")
    tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
    model = AutoModelForCausalLM.from_pretrained(
        MODEL_NAME,
        torch_dtype=torch.float16 if device == "cuda" else torch.float32
    )
    model = model.to(device)
    model.eval()
    print("✅ Local LLM components re-loaded")

messages = [
    {
        "role": "system",
        "content": "You are a productivity ai agent. Use only the supplied productivity context. Do not invent policies."
    },
    {
        "role": "user",
        "content": prompt
    }
]

formatted_prompt = tokenizer.apply_chat_template(
    messages,
    tokenize=False,
    add_generation_prompt=True
)

inputs = tokenizer(
    formatted_prompt,
    return_tensors="pt",
    truncation=True,
    max_length=4096
).to(device)

with torch.no_grad():
    output = model.generate(
        **inputs,
        max_new_tokens=250,
        do_sample=False
    )

new_tokens = output[0][inputs["input_ids"].shape[1]:]

answer = tokenizer.decode(
    new_tokens,
    skip_special_tokens=True
)

print("ANSWER")
print("=" * 60)
print(answer)


print("SOURCES USED")
print("-" * 50)

seen = set()

for chunk in retrieved_chunks:
    citation = (chunk["source"], chunk["page"])

    if citation not in seen:
        print(f"• {chunk['source']} — Page {chunk['page']}")
        seen.add(citation)



print("Documents in the knowledge base:")

for source in sorted(set(chunk["source"] for chunk in chunks)):
    print(" -", source)

print("\nTotal searchable chunks:", collection.count())



print("Retrieved evidence for evaluation:")
for rank, chunk in enumerate(retrieved_chunks, start=1):
    print(
        f"{rank}. {chunk['source']} | "
        f"Page {chunk['page']} | "
        f"distance={chunk['distance']:.4f}"
    )
