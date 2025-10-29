from fastapi import APIRouter
import app.constants as constants

router = APIRouter(tags=["common"])

@router.get(constants.BASE_ROUTE)
def base_root():
    return { "message": "Hello World!" }

@router.get(constants.HEALTH_CHECK_ROUTE)
def read_root():
    return { "System status": "Ok" }