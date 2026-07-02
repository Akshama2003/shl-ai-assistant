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

    # Detect intent
    state = route(state)

    # Off-topic
    if state["intent"] == "refuse":
        state["response"] = load_prompt("refusal.txt")
        return state

    # Ask clarification first
    if state["clarification_needed"]:
        state["response"] = (
            "I'd be happy to recommend SHL assessments.\n\n"
            "Could you please tell me:\n"
            "• Which role are you hiring for?\n"
            "• What is the seniority level?\n"
            "• Is this for hiring or employee development?"
        )
        return state

    # Retrieve assessments
    state["search_results"] = semantic_search(
        query,
        top_k=10
    )

    # Compare
    if state["intent"] == "compare":

        state["response"] = compare(
            query,
            state["search_results"]
        )

        return state

    # Refinement
    if state["refinement"]:

        state["response"] = (
            "I've updated the recommendations based on your latest requirements.\n\n"
            + recommend(
                query,
                state["search_results"]
            )
        )

        return state

    # Default recommendation

    state["response"] = recommend(
        query,
        state["search_results"]
    )

    return state