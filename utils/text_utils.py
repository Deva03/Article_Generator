import re

def word_count(text: str) -> int:
    words = re.findall(r"\b\w+\b", text)
    return len(words)
