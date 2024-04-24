from fastapi import APIRouter
from .endpoints import usecase

router = APIRouter()
router.include_router(usecase.router)
