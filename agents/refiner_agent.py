from langchain_core.messages import HumanMessage
from LLM.refiner_llm import refiner_llm
from Prompts.refiner_prompt import REFINER_PROMPT
from utils.logger import setup_logger
logger = setup_logger()

def refiner_agent(state):
    logger.info("")
    logger.info("")
    logger.info("")
    logger.info("")
    logger.info("--------------- In Refiner Agent --------------")
    logger.info("")

    article = state["draft_article"]
    evaluation = state.get("evaluation", "")

    prompt = REFINER_PROMPT.format(
        article=article,
        evaluation=evaluation
    )

    response = refiner_llm.invoke([
        HumanMessage(content=prompt)
    ])

    logger.info(f"Final Article as per Refiner LLM:{response.content.strip()}")

    return {
        "final_article": response.content.strip()
    }
