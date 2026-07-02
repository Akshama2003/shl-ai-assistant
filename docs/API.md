# API Documentation

## GET /health

Returns:

```json
{
  "status":"ok"
}
```

---

## POST /chat

Request

```json
{
  "messages":[
    {
      "role":"user",
      "content":"Hiring a Java developer"
    }
  ]
}
```

Response

```json
{
  "reply":"...",
  "recommendations":[
    {
      "name":"Java 8 (New)",
      "url":"...",
      "test_type":"K"
    }
  ],
  "end_of_conversation":true
}
```