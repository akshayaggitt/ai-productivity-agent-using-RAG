# AI Personal Productivity Assistant — RAG

A Retrieval-Augmented Generation (RAG) based personal productivity assistant that retrieves relevant information from a productivity knowledge base and uses a local language model to generate grounded responses.

The system is designed to answer productivity-related queries using information retrieved from user-provided PDF documents rather than relying only on the language model's internal knowledge.

---

## Overview

This project implements a complete RAG pipeline for a personal productivity assistant.

The system takes productivity information stored in PDF documents, extracts and chunks the content, converts the chunks into vector embeddings, stores them in ChromaDB, retrieves the most relevant information for a user query, and provides the retrieved context to a locally running Qwen language model.

### Pipeline

```text
PDF Knowledge Base
        ↓
Text Extraction
        ↓
Text Chunking
        ↓
Sentence Embeddings
        ↓
ChromaDB Vector Store
        ↓
Similarity Search
        ↓
Relevant Context
        ↓
Local Qwen LLM
        ↓
Grounded Response
