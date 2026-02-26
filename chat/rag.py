import json
import os
import numpy as np
from openai import OpenAI

client = OpenAI(api_key="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")

EMBED_MODEL = "text-embedding-3-small"
LLM_MODEL = "gpt-4o-mini"

SIMILARITY_THRESHOLD = 0.75
TOP_K = 3


def load_documents():
    path = os.path.join(os.path.dirname(__file__), "data.json")
    with open(path, "r") as f:
        return json.load(f)


def chunk_text(text, chunk_size=300):
    words = text.split()
    chunks = []
    for i in range(0, len(words), chunk_size):
        chunks.append(" ".join(words[i:i+chunk_size]))
    return chunks


def get_embedding(text):
    response = client.embeddings.create(
        model=EMBED_MODEL,
        input=text
    )
    return response.data[0].embedding


class VectorStore:
    def __init__(self):
        self.texts = []
        self.vectors = []

    def add(self, text, embedding):
        self.texts.append(text)
        self.vectors.append(np.array(embedding))

    def search(self, query_embedding):
        scores = []
        for vec in self.vectors:
            score = np.dot(vec, query_embedding) / (
                np.linalg.norm(vec) * np.linalg.norm(query_embedding)
            )
            scores.append(score)

        top_indices = np.argsort(scores)[::-1][:TOP_K]
        results = []

        for idx in top_indices:
            if scores[idx] >= SIMILARITY_THRESHOLD:
                results.append((self.texts[idx], scores[idx]))

        return results


vector_store = VectorStore()


def build_vector_store():
    docs = load_documents()
    for doc in docs:
        chunks = chunk_text(doc["content"])
        for chunk in chunks:
            embedding = get_embedding(chunk)
            vector_store.add(chunk, embedding)


#build_vector_store()
