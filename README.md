# SHL Conversational Assessment Recommender

A conversational AI assistant that recommends SHL assessments based on natural language queries. The assistant is built using FastAPI and the official SHL Individual Test Solutions catalog.

---

## Features

- Conversational assessment recommendation
- Clarification questions for vague queries
- Recommendation refinement
- Assessment comparison
- Prompt injection protection
- Off-topic refusal
- Uses official SHL assessment catalog
- REST API with FastAPI
- Ready for deployment on Render

---

## Project Structure

```
backend/
│
├── app/
│   ├── agent/
│   ├── api/
│   ├── retriever/
│   ├── scraper/
│   ├── models/
│   └── utils/
│
├── data/
│   └── catalog.json
│
├── prompts/
│
├── vector_db/
│
tests/
```

---

## Installation

Clone repository

```bash
git clone https://github.com/Akshama2003/shl-ai-assistant.git
```

Go inside

```bash
cd shl-ai-assistant/backend
```

Create virtual environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Linux

```bash
source .venv/bin/activate
```

Install requirements

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env`

```
GEMINI_API_KEY=YOUR_KEY
```

---

## Run

```bash
uvicorn app.main:app --reload
```

---

## API

Health

```
GET /health
```

Chat

```
POST /chat
```

---

## Example Request

```json
{
    "messages":[
        {
            "role":"user",
            "content":"Need Java Backend Developer assessment"
        }
    ]
}
```

---

## Example Response

```json
{
    "reply":"Based on your requirements...",
    "recommendations":[
        {
            "name":"Java 8 (New)",
            "url":"https://www.shl.com/products/product-catalog/view/java-8-new/",
            "test_type":"Knowledge & Skills"
        }
    ],
    "end_of_conversation":true
}
```

---

## Deployment

Hosted using Render

```
https://shl-ai-assistant-jfj6.onrender.com
```

---

## Tech Stack

- Python
- FastAPI
- Uvicorn
- Render
- JSON Catalog
- BeautifulSoup
- Requests

---

## Author

Akshama Chauhan
