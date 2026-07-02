def recommend(query, documents):
    if not documents:
        return "I couldn't find any matching SHL assessments."

    response = "Based on your requirements, I recommend:\n\n"

    for doc in documents[:5]:
        response += (
            f"- {doc.get('title', doc.get('name','Unknown'))}\n"
        )

    return response