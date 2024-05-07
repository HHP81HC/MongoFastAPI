# My Stuff
from src.schemas.student import StudentModel
from src.schemas.student import StudentCollection
from src.schemas.student import UpdateStudentModel
from src.controllers.student.common import student_repository

from fastapi import Body
from fastapi import APIRouter
from fastapi import status


def get_student_router() -> APIRouter:
    router = APIRouter()

    # Common routers
    @router.post(
        "/students",
        response_description="Add new student",
        response_model=StudentModel,
        status_code=status.HTTP_201_CREATED,
        response_model_by_alias=False,
        tags=["StudentController"]
    )
    async def create_student(student: StudentModel = Body(...)):
        return await student_repository.create_student(student)

    @router.get(
        "/students",
        response_description="List all students",
        response_model=StudentCollection,
        response_model_by_alias=False,
        tags=["StudentController"]
    )
    async def list_students():
        return await student_repository.list_students()

    @router.get(
        "/students/{id}",
        response_description="Get a single student",
        response_model=StudentModel,
        response_model_by_alias=False,
        tags=["StudentController"]
    )
    async def show_student(id: str):
        return await student_repository.show_student(id)

    @router.put(
        "/students/{id}",
        response_description="Update a student",
        response_model=StudentModel,
        response_model_by_alias=False,
        tags=["StudentController"]
    )
    async def update_student(id: str, student: UpdateStudentModel = Body(...)):
        return await student_repository.update_student(id, student)

    @router.delete(
        "/students/{id}",
        response_description="Delete a student",
        tags=["StudentController"]
    )
    async def delete_student(id: str):
        return await student_repository.delete_student(id)

    return router
