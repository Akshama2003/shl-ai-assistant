import json
import re
from pathlib import Path

CATALOG_PATH = Path("data/catalog.json")


def load_catalog():
    with open(CATALOG_PATH, "r", encoding="utf8") as f:
        return json.load(f)


catalog = load_catalog()


def normalize(text):
    return re.sub(r"[^a-z0-9+#. ]", " ", str(text).lower())


def text_field(value):
    if isinstance(value, list):
        return " ".join(str(v) for v in value)
    return str(value or "")


def score_document(query: str, doc: dict):
    q = normalize(query)
    words = [w for w in q.split() if len(w) > 1]

    name = normalize(doc.get("name", ""))
    description = normalize(doc.get("description", ""))
    keys = normalize(text_field(doc.get("keys", [])))
    job_levels = normalize(text_field(doc.get("job_levels", [])))
    languages = normalize(text_field(doc.get("languages", [])))
    duration = normalize(doc.get("duration", ""))

    full_text = " ".join([name, description, keys, job_levels, languages, duration])

    score = 0

    for word in words:
        if word in name:
            score += 20
        if word in keys:
            score += 10
        if word in description:
            score += 6
        if word in job_levels:
            score += 4
        if word in languages:
            score += 1

    role_boosts = {
        "java": ["java", "j2ee", "enterprise java", "core java"],
        "python": ["python"],
        "sql": ["sql", "database"],
        "excel": ["excel", "spreadsheet"],
        "manager": ["opq", "leadership", "management", "personality"],
        "leadership": ["opq", "leadership", "personality"],
        "personality": ["opq", "personality", "behavior"],
        "cognitive": ["verify", "ability", "reasoning", "numerical", "verbal", "deductive", "inductive"],
        "customer": ["contact center", "customer", "service"],
        "support": ["contact center", "customer", "service"]
    }

    for trigger, targets in role_boosts.items():
        if trigger in q:
            for target in targets:
                if target in full_text:
                    score += 15

    return score


def semantic_search(query: str, top_k: int = 10):
    scored = []

    for doc in catalog:
        if doc.get("status") and doc.get("status") != "ok":
            continue

        score = score_document(query, doc)

        if score > 0:
            scored.append((score, doc))

    scored.sort(key=lambda x: x[0], reverse=True)

    return [doc for _, doc in scored[:top_k]]