# AI Productivity Agent — RAG

A Retrieval-Augmented Generation (RAG) system designed to provide context-aware responses using a personal productivity knowledge base.

The system retrieves relevant information from a knowledge base and provides that context to an LLM before generating a response. The current implementation focuses on experimenting with document ingestion, chunking, embeddings, vector search, retrieval, and LLM-based generation.

## Overview

The idea behind this project is to explore how RAG can be used to give an AI system persistent contextual knowledge about a user's goals, projects, tasks, preferences, previous plans, and productivity patterns.

Instead of relying only on the information present in the current prompt, the system retrieves relevant information from previously stored documents.

For example:

```text
User Query
    ↓
"What should I prioritize today?"
    ↓
Retrieve relevant context
    ↓
Goals + Previous Plans + Deadlines + Preferences
    ↓
LLM
    ↓
Context-aware response
```

## Problem

A normal LLM conversation does not automatically have access to a user's complete historical context.

For a productivity assistant, useful information may exist across different documents and time periods:

- Long-term goals
- Current projects
- Previous daily plans
- Unfinished work
- Productivity reflections
- Scheduling preferences
- Deadlines
- Calendar information
- Learning priorities

Sending all of this information to the LLM for every query would be inefficient and would unnecessarily increase the context size.

RAG solves this by retrieving only the information relevant to the current query.

## RAG Pipeline

The current system follows this general pipeline:

```text
Knowledge Base
      ↓
Document Loading
      ↓
Text Extraction
      ↓
Chunking
      ↓
Embedding Generation
      ↓
Vector Database
      ↓
Similarity Search
      ↓
Relevant Chunks
      ↓
Prompt Construction
      ↓
LLM
      ↓
Generated Response
```

### 1. Document Loading

The knowledge base contains documents with productivity-related information.

The current knowledge base includes synthetic information such as:

- User goals
- Current focus areas
- Projects
- Productivity preferences
- Scheduling preferences
- Placement preparation priorities
- AI engineering learning priorities
- Reading interests
- Example tasks
- Historical daily plans
- Productivity reflections
- Upcoming deadlines
- Calendar constraints

### 2. Text Extraction

Documents such as PDFs are processed to extract their textual content.

### 3. Chunking

The extracted text is divided into smaller chunks before generating embeddings.

Chunking allows the retriever to return focused pieces of information instead of retrieving an entire document for every query.

### 4. Embeddings

Each chunk is converted into a numerical vector representation.

Conceptually:

```text
"AI project took longer than expected"
                ↓
          Embedding Model
                ↓
       [0.021, -0.183, ...]
```

Semantically similar pieces of information have similar vector representations.

### 5. Vector Database

The embeddings are stored in a vector database so that relevant information can be retrieved using semantic similarity.

The initial implementation can use a local vector database such as Chroma or FAISS.

### 6. Retrieval

When the user submits a query, the query is converted into an embedding and compared against stored vectors.

The system retrieves the most relevant chunks.

For example:

```text
Query:
"What should I prioritize today?"

Retrieved context:

1. Recent unfinished tasks
2. Upcoming deadlines
3. Current goals
4. Previous daily plan
5. Scheduling preferences
```

### 7. LLM Generation

The retrieved context is included in the prompt sent to the LLM.

The LLM then generates a response using both:

- The user's current query
- Retrieved knowledge

## Knowledge Base

The current knowledge base is designed as a test dataset for a personal productivity RAG system.

It contains different types of information so that retrieval can be evaluated across multiple semantic categories.

### User Goals

Examples include:

- Product engineering career preparation
- DSA proficiency
- Building a strong project portfolio
- AI engineering
- Communication
- Reading and personal development

### Current Focus Areas

Examples include:

- Placement preparation
- DSA
- Java programming
- AI project development
- Software engineering fundamentals
- Technical project building

### Projects

The knowledge base contains contextual information about projects such as:

- A RAG-powered AI productivity agent
- A metro passenger self-service locker concept
- A placement preparation system

### Historical Information

Previous daily plans contain:

- Planned tasks
- Completed tasks
- Unfinished tasks
- Reflections
- Planning implications

This allows the RAG system to answer questions that require historical context.

### Preferences

The knowledge base includes example preferences related to:

- Focus sessions
- Breaks
- Scheduling buffers
- Morning vs. evening work
- Avoiding excessive context switching
- Realistic workloads

## Example Queries

The system can be tested with questions such as:

```text
What are my long-term goals?

What am I currently focusing on?

What unfinished work should I consider today?

What happened during my previous daily plans?

Why did my AI project take longer than expected?

What are my highest-priority placement preparation areas?

What are my scheduling preferences?

Why should I leave buffer time in my schedule?

What project am I currently building?

What should I prioritize if I only have four hours today?

What patterns have appeared in my previous productivity reflections?

What deadline should receive the highest priority?
```

The strongest RAG tests are questions where the answer is not contained in a single isolated chunk and requires retrieving context from different parts of the knowledge base.

## Example Retrieval

### Query

```text
Why should I leave buffer time in my schedule?
```

### Potential retrieved context

```text
Scheduling Preferences:
Avoid filling every available minute.

Historical Reflection:
College responsibilities consumed more time than expected.

Historical Reflection:
The user underestimated the time required for AI project architecture.

Productivity Rule:
Leave realistic buffer time for unexpected work and task overruns.
```

The LLM can then combine these retrieved pieces into a context-aware answer.

## Facts vs. Generated Responses

The system should distinguish between information retrieved from the knowledge base and conclusions generated by the LLM.

For example:

```text
RETRIEVED FACT
The AI project previously took longer than expected.

RETRIEVED FACT
The user prefers realistic schedules with buffer time.

LLM RECOMMENDATION
Allocate a longer uninterrupted block for the AI project and leave
additional buffer time.
```

The recommendation is generated by the model; it should not be treated as an existing fact in the knowledge base.

## RAG vs. Structured Data

RAG is useful for semantic and historical context, but it should not necessarily be the source of truth for structured information.

For example:

```text
RAG / Vector Database
---------------------
Goals
Preferences
Historical plans
Project descriptions
Reflections
Notes

Structured Database
-------------------
Current task status
Exact deadlines
Scheduled start/end times
Task IDs
Completion status
```

This separation becomes important when building systems that need reliable state.

For example, an old document might say:

```text
Java assignment — pending
```

while the current task database says:

```text
Java assignment — completed
```

The current structured state should take precedence.

## Metadata

Useful metadata for indexed chunks can include:

```text
source_type
date
project
topic
task_id
status
priority
content_type
```

Example:

```text
content_type: reflection
date: 2026-09-08
project: AI productivity agent
topic: productivity
```

Metadata can be used alongside semantic similarity to improve retrieval quality.

## Technology Stack

| Component | Technology |
|---|---|
| Programming Language | Python |
| LLM | OpenAI API |
| RAG | Retrieval-Augmented Generation |
| Embeddings | Embedding model |
| Vector Database | Chroma / FAISS |
| Document Processing | PyPDF |
| Development Environment | Google Colab |
| Version Control | Git / GitHub |

The exact libraries and models may change during experimentation.

## Project Structure

The codebase can be organized as:

```text
ai-productivity-agent/
│
├── src/
│   ├── ingestion.py
│   ├── embeddings.py
│   ├── retrieval.py
│   ├── llm.py
│   └── main.py
│
├── data/
│   └── knowledge_base.pdf
│
├── tests/
│
├── requirements.txt
├── .gitignore
└── README.md
```

The structure may change as the implementation evolves.

## Current Implementation

The current focus of the repository is the RAG pipeline itself:

```text
PDF
 ↓
Extract text
 ↓
Create chunks
 ↓
Generate embeddings
 ↓
Store vectors
 ↓
Retrieve relevant chunks
 ↓
Send context to LLM
 ↓
Generate response
```

The repository is intended to document and preserve the current implementation rather than make assumptions about future features.

## Limitations

The current system has several limitations:

- The knowledge base is synthetic test data.
- Retrieved context may not always be sufficient to answer complex planning questions.
- Semantic similarity does not guarantee that retrieved information is factually current.
- The LLM may generate recommendations that are not explicitly present in the knowledge base.
- Exact task state is better handled by structured storage.
- Retrieval quality depends on chunking, embeddings, query formulation, and vector search configuration.

## Privacy

The current knowledge base uses synthetic information for development and testing.

Real personal information should not be committed to a public repository.

API keys and credentials should never be stored directly in source code.

Use environment variables or a secrets-management mechanism instead.

## Status

**Current stage:** RAG prototype

**Primary focus:** Document ingestion, chunking, embeddings, vector retrieval, and context-aware LLM generation.
