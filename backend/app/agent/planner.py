from app.agent.guardrails import is_prompt_injection


def detect_intent(query: str):
    q = query.lower()

    if is_prompt_injection(query):
        return "refuse"

    off_topic_words = [
        "weather", "football", "ipl", "movie", "recipe",
        "legal", "law", "politics", "python code"
    ]

    if any(word in q for word in off_topic_words):
        return "refuse"

    if any(word in q for word in ["compare", "difference", "vs", "versus"]):
        return "compare"

    if any(word in q for word in [
        "recommend", "suggest", "assessment", "test",
        "hire", "hiring", "developer"
    ]):
        return "recommend"

    return "general"


def needs_clarification(query: str):
    q = query.lower()

    if "compare" in q or "difference" in q or " vs " in q:
        return False

    if "user:" in q and "assistant:" in q:
        return False

    if len(q.split()) < 5:
        return True

    vague_phrases = [
        "i need an assessment",
        "need assessment",
        "suggest test",
        "recommend test"
    ]

    return q.strip() in vague_phrases


def is_refinement(query: str):
    q = query.lower()

    refinement_words = [
        "actually",
        "also",
        "include",
        "add",
        "remove",
        "instead",
        "change",
        "only",
        "exclude"
    ]

    return any(word in q for word in refinement_words)