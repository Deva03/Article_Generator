import os
from langchain_community.utilities import GoogleSerperAPIWrapper
from config.settings import SEARCH_RESULTS_LIMIT
from utils.web_page_loader import extract_page_content
from utils.logger import setup_logger

logger = setup_logger()


def search_agent(state):
    logger.info("")
    logger.info("")
    logger.info("")
    logger.info("")
    logger.info("--------------- In Search Agent --------------")
    logger.info("")

    if not os.getenv("SERPER_API_KEY"):
        raise ValueError("SERPER_API_KEY environment variable is not set")

    search = GoogleSerperAPIWrapper(k=SEARCH_RESULTS_LIMIT)

    query = state["topic"]
    results = search.results(query)

    logger.info(f"The chosed topic by User is: {query}")
    logger.info(f"Based on Google's API search we are getting these results::"
                f"{results}")

    enriched_results = []

    for r in results.get("organic", []):
        url = r.get("link")

        page_data = extract_page_content(url)

        if not page_data["valid"]:
            continue  # 🔥 FILTER APPLIED HERE

        enriched_results.append({
            "title": r.get("title"),
            "snippet": r.get("snippet"),
            "link": url,
            "content": page_data["content"],
            "word_count": page_data["word_count"]
        })

    logger.info(f"After applying filter to Serach Results: "
                f"{enriched_results}")

    return {
        "search_results": enriched_results
    }
