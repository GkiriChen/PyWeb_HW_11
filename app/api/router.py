from fastapi import APIRouter

from api.course import router as course_router

router = APIRouter(prefix="/v1")

router.include_router(course_router)
