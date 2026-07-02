from app.agent.router import route
from app.retriever.search import semantic_search
from app.agent.recommend import recommend
from app.agent.compare import compare
from app.agent.prompts import load_prompt


def run_agent(query: str):
    state = {
        "user_query": query,
        "intent": "",
        "clarification_needed": False,
        "refinement": False,
        "search_results": [],
        "response": ""
    }

    state = route(state)

    if state["intent"] == "refuse":
        state["response"] = load_prompt("refusal.txt")
        return state

    if state["clarification_needed"]:
        state["response"] = (
            "Could you provide more details about the role, skills, or seniority?"
        )
        return state

    state["search_results"] = semantic_search(
        query,
        top_k=10
    )

    if state["intent"] == "compare":
        state["response"] = compare(
            query,
            state["search_results"]
        )
    else:
        state["response"] = recommend(
            query,
            state["search_results"]
        )

    return state