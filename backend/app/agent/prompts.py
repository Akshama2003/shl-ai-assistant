from pathlib import Path

PROMPT_DIR = Path("prompts")


def load_prompt(filename):

    with open(
        PROMPT_DIR / filename,
        encoding="utf8"
    ) as f:

        return f.read()