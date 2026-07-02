import json
from pathlib import Path

CATALOG_PATH = Path("data/catalog.json")


def load_catalog():
    with open(CATALOG_PATH, "r", encoding="utf8") as f:
        return json.load(f)


catalog = load_catalog()


def text_field(value):
    if isinstance(value, list):
        return " ".join(str(v) for v in value)
    return str(value or "")


def score_document(query: str, doc: dict):
    q = query.lower()
    words = q.split()

    name = text_field(doc.get("name")).lower()
    description = text_field(doc.get("description")).lower()
    keys = text_field(doc.get("keys")).lower()
    job_levels = text_field(doc.get("job_levels")).lower()
    languages = text_field(doc.get("languages")).lower()

    score = 0

    for word in words:
        if word in name:
            score += 10
        if word in keys:
            score += 6
        if word in description:
            score += 4
        if word in job_levels:
            score += 3
        if word in languages:
            score += 1

    return score


def semantic_search(query: str, top_k: int = 10):
    scored = []

    for doc in catalog:
        if doc.get("status") != "ok":
            continue

        score = score_document(query, doc)

        if score > 0:
            scored.append((score, doc))

    scored.sort(key=lambda x: x[0], reverse=True)

    return [doc for _, doc in scored[:top_k]]