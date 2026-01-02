from typing import TypedDict, Optional, List, Dict

class ArticleState(TypedDict):
    topic: str

    temperature: float               # user-controlled
    revised_temperature: Optional[float]  # evaluator suggested

    search_results: Optional[List[Dict]]

    retry_count: int            # ← NEW
    draft_article: Optional[str]
    evaluation_score: Optional[float]
    evaluation_feedback: Optional[str]

    final_article: Optional[str]
    html_content: Optional[str]
