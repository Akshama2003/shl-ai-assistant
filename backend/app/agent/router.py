from app.agent.planner import (
    detect_intent,
    needs_clarification,
    is_refinement
)


def route(state):
    state["intent"] = detect_intent(state["user_query"])

    state["clarification_needed"] = needs_clarification(
        state["user_query"]
    )

    state["refinement"] = is_refinement(
        state["user_query"]
    )

    return state