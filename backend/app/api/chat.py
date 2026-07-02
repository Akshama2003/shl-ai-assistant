from fastapi import APIRouter

from app.agent.conversation import build_conversation
from app.agent.graph import run_agent
from app.models.request import ChatRequest
from app.models.response import ChatResponse, Recommendation
from app.agent.guardrails import is_valid_catalog_url

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
async def chat(request: ChatRequest):
    query = build_conversation(request.messages)

    state = run_agent(query)

    recommendations = []

    for doc in state["search_results"][:10]:
        url = doc.get("url", "")

        if not is_valid_catalog_url(url):
            continue

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