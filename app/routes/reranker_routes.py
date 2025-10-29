from fastapi import APIRouter, Body
from typing import List, Dict, Any
import app.constants as constants
from app.services.reranker_service import RerankerService

router = APIRouter(prefix=constants.RERANKER_ROUTES_PREFIX, tags=["reranker"])

reranker_service_instance = RerankerService()

@router.post(constants.RERANKER_ROUTE)
def rerank_items(
    query: str = Body(..., embed=True),
    items: List[Dict[str, Any]] = Body(..., embed=True)
):
    ranked_items = reranker_service_instance.rerank(query, items)
    return { "ranked_items": ranked_items }