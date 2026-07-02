from app.agent.prompts import load_prompt
from app.agent.llm import ask_llm


def compare(query: str, documents: list):
    prompt = load_prompt("compare.txt")

    prompt = prompt.replace("{query}", query)
    prompt = prompt.replace("{documents}", str(documents[:10]))

    return ask_llm(prompt)