import requests
from readability import Document
from bs4 import BeautifulSoup
from utils.text_utils import word_count

HEADERS = {
    "User-Agent": "Mozilla/5.0 (compatible; ZenaraBot/1.0)"
}

def extract_page_content(
    url: str,
    min_words: int = 700,
) -> dict:
    try:
        response = requests.get(url, headers=HEADERS, timeout=10)
        response.raise_for_status()

        doc = Document(response.text)
        html = doc.summary()

        soup = BeautifulSoup(html, "html.parser")
        text = soup.get_text(separator="\n")

        cleaned_text = "\n".join(
            line.strip() for line in text.splitlines() if line.strip()
        )

        wc = word_count(cleaned_text)

        if wc > min_words:
            return {
                "valid": False,
                "word_count": wc,
                "content": ""
            }

        return {
            "valid": True,
            "word_count": wc,
            "content": cleaned_text[:]
        }

    except Exception as e:
        return {
            "valid": False,
            "word_count": 0,
            "content": ""
        }
