# SHL Conversational Assessment Recommender

## Overview

This project implements a conversational AI assistant that recommends SHL Individual Test Solutions using a Retrieval-Augmented Generation (RAG) architecture.

The assistant is designed to:

- Clarify vague hiring requirements.
- Recommend relevant SHL assessments.
- Support follow-up refinements.
- Compare SHL assessments.
- Refuse off-topic or unsafe requests.
- Only recommend assessments present in the SHL catalog.

---

## System Architecture

User

↓

FastAPI

↓

Conversation Builder

↓

Intent Planner

↓

Semantic Search (FAISS)

↓

CrossEncoder Re-ranker

↓

Gemini

↓

JSON Response

---

## Retrieval Pipeline

The SHL catalog is scraped and stored as structured JSON.

Each assessment is embedded using:

all-MiniLM-L6-v2

Embeddings are stored inside a FAISS vector index.

For every query:

1. Generate embedding.
2. Retrieve Top-20 candidates.
3. Re-rank using CrossEncoder.
4. Keep Top-10.
5. Pass retrieved assessments to Gemini.

This reduces hallucinations and improves Recall@10.

---

## Conversation Flow

The API is stateless.

Every POST /chat request contains the complete conversation history.

The assistant supports:

- Clarification
- Recommendation
- Refinement
- Comparison
- Refusal

without storing server-side state.

---

## Prompt Design

Five prompt templates are used.

- system.txt
- recommend.txt
- compare.txt
- clarify.txt
- refusal.txt

The prompts instruct Gemini to only use retrieved SHL catalog data.

---

## Guardrails

The assistant includes:

- Prompt injection detection
- Off-topic detection
- URL validation
- Catalog-only recommendations

---

## Technology Stack

Backend

- FastAPI
- Python

Retrieval

- Sentence Transformers
- FAISS
- CrossEncoder

LLM

- Gemini

Deployment

- Docker
- Render

---

## Evaluation

The project was evaluated using:

- Health endpoint tests
- Chat schema tests
- Clarification tests
- Refusal tests
- Recommendation tests

The design aligns with SHL's evaluation criteria:

- Schema compliance
- Recall@10
- Clarification behavior
- Refinement
- Comparison
- Prompt injection resistance