from fastapi import APIRouter
import app.constants as constants

from app.routes.base import router as common_router
from app.routes.embedding_routes import router as embedding_routes
from app.routes.reranker_routes import router as reranker_routes
from app.routes.auto_tagger_routes import router as auto_tagger_routes

router = APIRouter(prefix=constants.API_PREFIX)

router.include_router(common_router)
router.include_router(embedding_routes)
router.include_router(reranker_routes)
router.include_router(auto_tagger_routes)