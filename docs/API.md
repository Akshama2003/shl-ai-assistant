# API Documentation

## Base URL

```
https://shl-ai-assistant-jfj6.onrender.com
```

---

# GET /health

Returns service health.

### Response

```json
{
    "status":"ok"
}
```

---

# POST /chat

Accepts complete conversation history.

### Request

```json
{
    "messages":[
        {
            "role":"user",
            "content":"Need Java Developer assessment"
        }
    ]
}
```

---

### Response

```json
{
    "reply":"Based on your requirements...",
    "recommendations":[
        {
            "name":"Java 8",
            "url":"https://www.shl.com/...",
            "test_type":"Knowledge & Skills"
        }
    ],
    "end_of_conversation":true
}
```