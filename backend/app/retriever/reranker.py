from sentence_transformers import CrossEncoder

model = CrossEncoder("cross-encoder/ms-marco-MiniLM-L-6-v2")


def rerank(query, documents, top_k=10):
    """
    Re-rank retrieved documents based on relevance to the query.
    """

    if not documents:
        return []

    pairs = []

    for doc in documents:
        text = " ".join([
            doc.get("title", ""),
            doc.get("description", ""),
            doc.get("category", "")
        ])
        pairs.append((query, text))

    scores = model.predict(pairs)

    ranked = sorted(
        zip(scores, documents),
        key=lambda x: x[0],
        reverse=True
    )

    return [doc for _, doc in ranked[:top_k]]