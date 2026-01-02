from langchain_core.messages import HumanMessage
from LLM.evaluator_llm import evaluator_llm
from Prompts.evaluator_prompt import EVALUATOR_PROMPT
from utils.logger import setup_logger
logger = setup_logger()


def evaluator_agent(state):
    logger.info("")
    logger.info("")
    logger.info("")
    logger.info("")
    logger.info("--------------- In Evaluator Agent --------------")
    logger.info("")

    prompt = EVALUATOR_PROMPT.format(
        article=state["draft_article"]
    )

    response = evaluator_llm.invoke([
        HumanMessage(content=prompt)
    ])

    content = response.content.strip()

    score = float(content.split("SCORE:")[1].split("\n")[0].strip())
    feedback = content.split("FEEDBACK:")[1].strip()

    revised_temp = None
    if "increase temperature" in feedback.lower():
        revised_temp = min(state["temperature"] + 0.1, 1.0)
    elif "reduce temperature" in feedback.lower():
        revised_temp = max(state["temperature"] - 0.1, 0.0)

    logger.info(f"Evaluation Results are as followed. (This is for this iteration)")
    logger.info(f"evaluation_score : {score}")
    logger.info(f"evaluation_feedback :{feedback}")
    logger.info(f"revised_temperature: {revised_temp}")

    return {
        "evaluation_score": score,
        "evaluation_feedback": feedback,
        "revised_temperature": revised_temp
    }
