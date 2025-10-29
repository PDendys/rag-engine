from fastapi import APIRouter, Body, Query
from app.services.embedding_service import EmbeddingService
import app.constants as constants

router = APIRouter(prefix=constants.EMBEDDING_ROUTES_PREFIX, tags=["embedding"])

embedding_service_instance = EmbeddingService()

@router.post(constants.CREATE_EMBEDDING_ROUTE)
def create_embedding_root(text: str = Body(..., embed=True)):
    embedding = embedding_service_instance.create_embedding(text)
    return { "embedding": embedding }

@router.get(constants.CREATE_EMBEDDING_ROUTE)
def create_embedding_root_get(text: str = Query(...)):
    embedding = embedding_service_instance.create_embedding(text)
    return { "embedding": embedding }