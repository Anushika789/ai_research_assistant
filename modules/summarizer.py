import streamlit as st
from transformers import pipeline

@st.cache_resource
def get_summarizer():
    return pipeline("summarization", model="facebook/bart-large-cnn")

summarizer = get_summarizer()

def ai_summarize(text, length=5):
    """
    Summarize the input text using a local Hugging Face model.
    Returns a summary string or a clear error message.
    """
    max_len = length * 20
    min_len = length * 10

    if not isinstance(text, str) or not text.strip():
        return "No content to summarize."

    try:
        summary_list = summarizer(text, max_length=max_len, min_length=min_len, do_sample=False)
        if not summary_list or 'summary_text' not in summary_list[0]:
            return f"Summary could not be generated. Model output: {summary_list}"
        return summary_list[0]['summary_text']
    except Exception as e:
        return f"Summary generation failed: {str(e)}"
