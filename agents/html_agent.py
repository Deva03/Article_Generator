from langchain_core.messages import HumanMessage
from LLM.html_llm import html_llm
from Prompts.html_prompt import HTML_PROMPT
from utils.logger import setup_logger
logger = setup_logger()

def html_agent(state):

    logger.info("")
    logger.info("")
    logger.info("")
    logger.info("")
    logger.info("--------------- In HTML Agent --------------")
    logger.info("")

    article = state["final_article"]

    prompt = HTML_PROMPT.format(article=article)

    response = html_llm.invoke([
        HumanMessage(content=prompt)
    ])

    html_content = response.content.strip()

    logger.info("The file is stored in HTML files folder")

    return {
        "html_content": html_content
    }
