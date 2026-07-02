import numpy as np

from app.retriever.embeddings import embed
from app.retriever.vector_store import load_vector_store


index, documents = load_vector_store()


def semantic_search(query, top_k=5):

    vector = embed([query])

    distances, indices = index.search(
        np.array(vector).astype("float32"),
        top_k
    )

    results = []

    for idx in indices[0]:

        results.append(documents[idx])

    return results[:top_k]