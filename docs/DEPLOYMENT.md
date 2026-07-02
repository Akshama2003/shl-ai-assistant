# Deployment Guide

## Local

Install requirements

```bash
pip install -r requirements.txt
```

Run

```bash
uvicorn app.main:app --reload
```

---

## Render

Root Directory

```
backend
```

Build Command

```bash
pip install -r requirements.txt
```

Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```

Environment Variables

```
GEMINI_API_KEY=...
```

---

## Health Endpoint

```
/health
```

---

## API Docs

```
/docs
```