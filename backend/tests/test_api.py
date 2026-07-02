from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "ok"


def test_chat_schema():
    response = client.post(
        "/chat",
        json={
            "messages": [
                {
                    "role": "user",
                    "content": "Hiring a Java developer with 4 years experience"
                }
            ]
        }
    )

    assert response.status_code == 200

    data = response.json()

    assert "reply" in data
    assert "recommendations" in data
    assert "end_of_conversation" in data
    assert isinstance(data["recommendations"], list)


def test_vague_query_clarifies():
    response = client.post(
        "/chat",
        json={
            "messages": [
                {
                    "role": "user",
                    "content": "Need assessment"
                }
            ]
        }
    )

    data = response.json()

    assert data["recommendations"] == []
    assert "details" in data["reply"].lower() or "role" in data["reply"].lower()


def test_off_topic_refusal():
    response = client.post(
        "/chat",
        json={
            "messages": [
                {
                    "role": "user",
                    "content": "Who won IPL?"
                }
            ]
        }
    )

    data = response.json()

    assert data["recommendations"] == []
    assert "shl" in data["reply"].lower()