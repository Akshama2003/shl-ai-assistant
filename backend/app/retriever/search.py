import json
from pathlib import Path


DATA_PATH = Path("data/catalog.json")


def load_catalog():
    with open(DATA_PATH, encoding="utf8") as f:
        return json.load(f)


documents = load_catalog()


def score_document(query: str, doc: dict):
    q_words = set(query.lower().split())

    text = " ".join([
        doc.get("title", ""),
        doc.get("name", ""),
        doc.get("description", ""),
        doc.get("category", ""),
        doc.get("test_type", "")
    ]).lower()

    score = 0

    for word in q_words:
        if word in text:
            score += 1

    return score


def semantic_search(query, top_k=10):
    ranked = sorted(
        documents,
        key=lambda doc: score_document(query, doc),
        reverse=True
    )

    return ranked[:top_k]