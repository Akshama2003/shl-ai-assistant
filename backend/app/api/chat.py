from fastapi import APIRouter

from app.agent.conversation import build_conversation
from app.agent.graph import run_agent
from app.models.request import ChatRequest
from app.models.response import ChatResponse, Recommendation

router = APIRouter()


def normalize_url(doc: dict):
    url = doc.get("url") or doc.get("link") or ""

    if not url:
        return "https://www.shl.com/"

    if url.startswith("/"):
        return "https://www.shl.com" + url

    return url


def get_test_type(doc: dict):
    keys = doc.get("keys", [])

    if isinstance(keys, list):
        return ", ".join(keys)

    return doc.get("test_type", "")


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    query = build_conversation(request.messages)

    state = run_agent(query)

    recommendations = []

    for doc in state["search_results"][:5]:
        recommendations.append(
            Recommendation(
                name=doc.get("name", doc.get("title", "")),
                url=normalize_url(doc),
                test_type=(
                    doc.get("category")
                    or ", ".join(doc.get("keys", [])[:2])
                    or doc.get("test_type", "")
                )
            )
        )

    return ChatResponse(
        reply=state["response"],
        recommendations=recommendations,
        end_of_conversation=len(recommendations) > 0
    )