from fastapi import APIRouter, Body, Query
import app.constants as constants
from app.services.auto_tagger_service import AutoTaggerService

router = APIRouter(prefix=constants.AUTO_TAGGER_ROUTES_PREFIX, tags=["auto_tagger"])

auto_tagger_service = AutoTaggerService()

@router.get(constants.AUTO_TAGGER_ROUTE)
def tag(text: str = Query(..., description="Text to tag")):
  return auto_tagger_service.get_tag(text)