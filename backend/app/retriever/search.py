import json
from pathlib import Path

CATALOG_PATH = Path("data/catalog.json")


def load_catalog():
    with open(CATALOG_PATH, "r", encoding="utf8") as f:
        return json.load(f)


catalog = load_catalog()


def semantic_search(query: str, top_k: int = 10):

    query = query.lower()

    scored = []

    for doc in catalog:

        score = 0

        title = doc.get("name", "").lower()

        description = doc.get("description", "").lower()

        category = doc.get("category", "").lower()

        skills = " ".join(doc.get("skills", [])).lower()

        roles = " ".join(doc.get("roles", [])).lower()

        for word in query.split():

            if word in title:
                score += 10

            if word in skills:
                score += 8

            if word in roles:
                score += 6

            if word in category:
                score += 4

            if word in description:
                score += 2

        if score > 0:
            scored.append((score, doc))

    scored.sort(reverse=True, key=lambda x: x[0])

    return [doc for _, doc in scored[:top_k]]