import asyncio
import pytest
from bson import ObjectId
from fastapi import HTTPException
from fastapi.responses import Response
from app.controllers.student.common import StudentCommonRepository
from app.schemas.student import StudentModel, UpdateStudentModel

# Define the student data
student_data = {
    "name": "Jane Doe",
    "email": "jdoe@example.com",
    "course": "Experiments, Science, and Fashion in Nanophotonics",
    "gpa": 3.0,
}


@pytest.fixture
def student_repo():
    # Setup any necessary dependencies or resources
    repo = StudentCommonRepository("test_collection")
    yield repo
    # Teardown any resources if needed


@pytest.mark.asyncio
async def test_create_document(student_repo):
    # Create a student document with the provided data
    created_student = await student_repo.create_document(StudentModel(**student_data))
    assert created_student is not None
    assert created_student["name"] == student_data["name"]
    assert created_student["email"] == student_data["email"]
    assert created_student["course"] == student_data["course"]
    assert created_student["gpa"] == student_data["gpa"]
    assert "_id" in created_student


@pytest.mark.asyncio
async def test_list_documents(student_repo):
    asyncio.get_running_loop()
    # Assuming some data exists in the database
    students = await student_repo.list_documents()
    assert len(students.students) > 0
