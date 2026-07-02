import json

import faiss
import numpy as np

from app.retriever.embeddings import embed

INDEX_PATH = "vector_db/index.faiss"
DATA_PATH = "data/catalog.json"

documents = []
index = None


def build_vector_store():
    global documents, index

    with open(DATA_PATH, encoding="utf-8") as f:
        documents = json.load(f)

    texts = []

    for doc in documents:
        text = " ".join(
            [
                doc.get("title", ""),
                doc.get("description", ""),
                doc.get("category", ""),
            ]
        )
        texts.append(text)

    vectors = embed(texts)

    dimension = vectors.shape[1]
    index = faiss.IndexFlatL2(dimension)

    index.add(np.array(vectors).astype("float32"))

    faiss.write_index(index, INDEX_PATH)

    print(f"Indexed {len(documents)} documents")


def load_vector_store():
    global documents, index

    with open(DATA_PATH, encoding="utf-8") as f:
        documents = json.load(f)

    index = faiss.read_index(INDEX_PATH)

    return index, documents