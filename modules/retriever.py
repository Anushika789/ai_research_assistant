import streamlit as st
import numpy as np
from sentence_transformers import SentenceTransformer

@st.cache_resource
def get_embedder():
    return SentenceTransformer('all-MiniLM-L6-v2')

embedder = get_embedder()

def get_embeddings(texts):
    if not texts or not isinstance(texts, list):
        return []
    try:
        return embedder.encode(texts, convert_to_numpy=True)
    except Exception as e:
        return []

def cosine_similarity(a, b):
    a, b = np.array(a), np.array(b)
    if np.linalg.norm(a) == 0 or np.linalg.norm(b) == 0:
        return 0.0
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def retrieve_relevant_passages(query, sections, top_k=3):
    if not query or not sections:
        return []
    section_texts = [sec[1] for sec in sections]
    section_embeddings = get_embeddings(section_texts)
    if not len(section_embeddings):
        return []
    query_embedding = get_embeddings([query])
    if not len(query_embedding):
        return []
    query_embedding = query_embedding[0]
    scored = [(i, cosine_similarity(query_embedding, emb)) for i, emb in enumerate(section_embeddings)]
    top_indices = sorted(scored, key=lambda x: x[1], reverse=True)[:top_k]
    return [sections[i] for i, _ in top_indices]
