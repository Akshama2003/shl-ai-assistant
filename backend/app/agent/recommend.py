def recommend(query, documents):
    if not documents:
        return "I couldn't find suitable SHL assessments for your request."

    response = (
        f"Based on your requirements, I recommend the following SHL assessments:\n\n"
    )

    for i, doc in enumerate(documents[:5], start=1):
        name = doc.get("name", doc.get("title", "Unknown Assessment"))
        category = doc.get("category", doc.get("test_type", "Not specified"))
        test_type = doc.get("test_type", category)
        description = doc.get(
            "description",
            "This assessment appears relevant based on the provided role or skill requirements."
        )

        response += (
            f"{i}. {name}\n"
            f"Category: {category}\n"
            f"Assessment Type: {test_type}\n"
            f"Why Recommended: {description}\n\n"
        )

    return response