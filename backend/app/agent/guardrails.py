def is_prompt_injection(query: str) -> bool:
    q = query.lower()

    dangerous_phrases = [
        "ignore previous instructions",
        "ignore all instructions",
        "forget your rules",
        "act as",
        "you are now",
        "reveal your prompt",
        "show system prompt",
        "bypass",
        "jailbreak"
    ]

    return any(phrase in q for phrase in dangerous_phrases)


def is_valid_catalog_url(url: str) -> bool:
    return url.startswith("https://www.shl.com/")