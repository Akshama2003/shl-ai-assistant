import os
from pathlib import Path

import google.generativeai as genai
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parents[2]   # backend/
load_dotenv(BASE_DIR / ".env")

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY not found in backend/.env")

genai.configure(api_key=api_key)

model = genai.GenerativeModel("gemini-2.5-flash")


def ask_llm(prompt: str):
    response = model.generate_content(prompt)
    return response.text