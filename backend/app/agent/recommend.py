def recommend(query, documents):
    if not documents:
        return (
            "Sorry, I couldn't find any matching SHL assessments. "
            "Could you provide more details about the role, skills, or job level?"
        )

    response = (
        "Based on your requirements, I recommend the following SHL assessments:\n\n"
    )

    for i, doc in enumerate(documents[:5], start=1):

        name = doc.get("name", "Unknown Assessment")

        category = (
            doc.get("category")
            or ", ".join(doc.get("keys", [])[:2])
            or "Not specified"
        )

        duration = doc.get("duration") or "Not specified"

        description = doc.get("description", "").strip()

        if len(description) > 180:
            description = description[:180].rsplit(" ", 1)[0] + "..."

        response += (
            f"**{i}. {name}**\n"
            f"Category: {category}\n"
            f"Duration: {duration}\n"
            f"Why Recommended: {description}\n\n"
        )

    response += (
        "These recommendations are based on your stated requirements. "
        "If you'd like, I can also recommend personality, cognitive, technical, "
        "or leadership assessments specifically."
    )

    return response