# SHL Conversational Assessment Recommender

## Problem Statement

Recruiters often describe hiring requirements in natural language rather than using predefined assessment names. This project converts conversational queries into relevant SHL assessment recommendations.

---

# Architecture

User Query

↓

Intent Detection

↓

Clarification

↓

Catalog Search

↓

Ranking

↓

Recommendation

↓

JSON Response

---

# Catalog

The application uses the SHL Individual Test Solutions catalog.

Each assessment contains:

- Name
- Description
- Duration
- Job Levels
- Languages
- Assessment Areas
- Remote Testing
- Adaptive Testing
- Official SHL URL

---

# Retrieval

The retrieval engine performs:

- keyword matching
- role matching
- skills matching
- assessment area matching
- business rule boosting

Results are ranked before recommendation.

---

# Agent Behaviour

The assistant supports:

- clarification
- recommendation
- refinement
- comparison
- prompt injection protection
- off-topic refusal

Conversation history is passed in every request, making the API stateless.

---

# Evaluation

The assistant was evaluated using the provided SHL public conversation traces.

The following scenarios were tested:

- vague requests
- recommendation
- comparison
- refinement
- prompt injection
- off-topic questions

---

# Trade-offs

A lightweight ranking approach was chosen over a large vector database to improve deployment speed and reduce memory usage on Render Free Tier.

---

# Future Improvements

- Hybrid retrieval
- Cross-encoder reranking
- Vector database
- LLM explanation generation
- Conversation memory