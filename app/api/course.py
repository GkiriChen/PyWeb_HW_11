from fastapi import APIRouter

router = APIRouter(prefix="/course/")


@router.get("/")
async def list_courses():
    return {}


@router.get("/course_id")
async def get_course_details(course_id: int):
    return {"course_id": course_id}
