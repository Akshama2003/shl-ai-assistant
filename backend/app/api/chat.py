from fastapi import APIRouter

from app.agent.conversation import build_conversation
from app.agent.graph import run_agent
from app.models.request import ChatRequest
from app.models.response import ChatResponse, Recommendation

router = APIRouter()


def normalize_url(url: str) -> str:
    if not url:
        return "https://www.shl.com/"

    if url.startswith("/"):
        return "https://www.shl.com" + url

    return url


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    query = build_conversation(request.messages)

    state = run_agent(query)

    recommendations = []

    for doc in state["search_results"][:10]:
        url = normalize_url(doc.get("url", ""))

        recommendations.append(
            Recommendation(
                name=doc.get("title", doc.get("name", "")),
                url=url,
                test_type=doc.get("category", doc.get("test_type", ""))
            )
        )

    end = len(recommendations) > 0

    return ChatResponse(
        reply=state["response"],
        recommendations=recommendations,
        end_of_conversation=end
    )