from langchain_core.messages import HumanMessage
from LLM.writer_llm import get_writer_llm
from Prompts.writer_prompt import WRITER_PROMPT
from utils.logger import setup_logger
logger = setup_logger()


def writer_agent(state):
    logger.info("")
    logger.info("--------------- In Writer Agent --------------")
    logger.info("")

    temperature = (
        state.get("revised_temperature")
        if state.get("revised_temperature") is not None
        else state["temperature"]
    )

    llm = get_writer_llm(temperature)

    prompt = WRITER_PROMPT.format(
        topic=state["topic"],
        search_results=state.get("search_results", []),
        feedback=state.get("evaluation_feedback", "None")
    )

    response = llm.invoke([
        HumanMessage(content=prompt)
    ])

    logger.info(f"This is the article written by LLM. With the temprature value of {temperature}")
    logger.info(f"Its retry count is :{state["retry_count"]}")
    cont = response.content
    logger.info(f"Draft Article Is as follows:"
                f"{cont}")

    return {
        "draft_article": response.content,
        "retry_count": state["retry_count"]+1
    }
