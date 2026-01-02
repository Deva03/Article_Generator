from langgraph.graph import StateGraph, END
from graph.state import ArticleState
from agents.search_agent import search_agent
from agents.writer_agent import writer_agent
from agents.evaluator_agent import evaluator_agent
from agents.html_agent import html_agent
from agents.refiner_agent import refiner_agent
from config.settings import EVALUATION_THRESHOLD, MAX_RETRIES

def should_continue(state):
    if state["evaluation_score"] >= EVALUATION_THRESHOLD:
        return "refiner"

    if state["retry_count"] >= MAX_RETRIES:
        return "refiner"   # force forward progress

    return "writer"


def build_graph():
    graph = StateGraph(ArticleState)

    graph.add_node("search", search_agent)
    graph.add_node("writer", writer_agent)
    graph.add_node("evaluator", evaluator_agent)
    graph.add_node("refiner", refiner_agent)

    graph.add_node("html_renderer", html_agent)

    graph.set_entry_point("search")

    graph.add_edge("search", "writer")
    graph.add_edge("writer", "evaluator")

    graph.add_conditional_edges(
        "evaluator",
        should_continue,
        {
            "writer": "writer",
            "refiner": "refiner"
        }
    )

    graph.add_edge("refiner", "html_renderer")
    graph.add_edge("html_renderer", END)

    return graph.compile()
