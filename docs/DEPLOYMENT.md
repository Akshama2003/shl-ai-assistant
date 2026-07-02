# Deployment

## Local

```bash
cd backend

uvicorn app.main:app --reload
```

Swagger

http://127.0.0.1:8000/docs

---

## Docker

```bash
docker build -t shl-ai-assistant .

docker run -p 8000:8000 shl-ai-assistant
```

---

## Render

Start Command

```bash
uvicorn app.main:app --host 0.0.0.0 --port $PORT
```