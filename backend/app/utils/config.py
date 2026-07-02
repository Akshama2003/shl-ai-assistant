from dotenv import load_dotenv

import os

load_dotenv()


class Settings:

    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    GROQ_API_KEY = os.getenv("GROQ_API_KEY")

    GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

    MODEL_NAME = os.getenv("MODEL_NAME")

    EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL")

    VECTOR_DB = os.getenv("VECTOR_DB")

    TOP_K = int(os.getenv("TOP_K", 10))


settings = Settings()