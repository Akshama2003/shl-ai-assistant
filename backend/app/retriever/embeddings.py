from sentence_transformers import SentenceTransformer

MODEL_NAME = "all-MiniLM-L6-v2"

model = SentenceTransformer(MODEL_NAME)


def embed(texts):
    """
    Convert list of strings into embeddings.
    """
    return model.encode(
        texts,
        show_progress_bar=True,
        convert_to_numpy=True
    )