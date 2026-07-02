def recommend(query, documents):
    if not documents:
        return "I couldn't find suitable SHL assessments for your request."

    response = "Based on your requirements, I recommend the following SHL assessments:\n\n"

    for i, doc in enumerate(documents[:5], start=1):
        name = doc.get("name", "Unknown Assessment")
        keys = doc.get("keys", [])
        duration = doc.get("duration", "Not specified")
        remote = doc.get("remote", "Not specified")
        adaptive = doc.get("adaptive", "Not specified")
        description = doc.get("description", "No description available.")

        if isinstance(keys, list):
            keys_text = ", ".join(keys)
        else:
            keys_text = str(keys)

        response += (
            f"{i}. {name}\n"
            f"Type: {keys_text}\n"
            f"Duration: {duration or 'Not specified'}\n"
            f"Remote Testing: {remote}\n"
            f"Adaptive: {adaptive}\n"
            f"Why Recommended: {description}\n\n"
        )

    return response