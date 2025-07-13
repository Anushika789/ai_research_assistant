# utils.py

import re

def highlight_text(text, keywords):
    """
    Highlights keywords in the text by wrapping them in a span with a background color.
    Returns HTML string.
    """
    if not keywords:
        return text
    pattern = re.compile(r'(' + '|'.join(map(re.escape, keywords)) + r')', re.IGNORECASE)
    return pattern.sub(r'<span style="background-color: #ffe066">\1</span>', text)

def truncate_text(text, max_words=150):
    """
    Truncates text to a maximum number of words.
    """
    words = text.split()
    if len(words) > max_words:
        return ' '.join(words[:max_words]) + '...'
    return text

def clean_text(text):
    """
    Removes extra whitespace and non-printable characters.
    """
    return ' '.join(text.split())
