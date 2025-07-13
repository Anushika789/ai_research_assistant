from modules.summarizer import ai_summarize
from modules.retriever import retrieve_relevant_passages

def answer_question(query, sections, language="English"):
    if not query or not sections:
        return "No question or document to answer.", []
    relevant = retrieve_relevant_passages(query, sections)
    if not relevant:
        return "No relevant passages found.", []
    context = "\n\n".join([f"{t or ''}: {txt}" for t, txt in relevant])
    prompt = (
        f"Based only on the following document passages, answer the question in {language}:\n\n"
        f"{context}\n\nQuestion: {query}\n\nAnswer with reference to the text."
    )
    answer = ai_summarize(prompt, length=3)
    return answer, relevant
