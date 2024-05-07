# Standard library
# My Stuff
from src.mongo_api.utils.client import db
from src.mongo_api.schemas.student import StudentModel
from src.mongo_api.schemas.student import StudentCollection
from src.mongo_api.schemas.student import UpdateStudentModel

from bson import ObjectId
from fastapi import Body
from fastapi import HTTPException
from fastapi import status
from pymongo import ReturnDocument
from motor.core import AgnosticCollection
from fastapi.responses import Response


class StudentCommonRepository:

    def __init__(self) -> None:
        """
        Initializes a new instance of the Common class.
        """
        # Get the collection from the database
        self.collection: AgnosticCollection = db.get_collection("students")

    async def create_student(self, student: StudentModel = Body(...)):
        """
        Insert a new student record.

        A unique `id` will be created and provided in the response.
        """
        new_student = await self.collection.insert_one(
            student.model_dump(by_alias=True, exclude=["id"])
        )
        created_student = await self.collection.find_one(
            {"_id": new_student.inserted_id}
        )
        return created_student

    async def list_students(self):
        """
        List all of the student data in the database.

        The response is unpaginated and limited to 1000 results.
        """
        print("Get all students")
        return StudentCollection(students=await self.collection.find().to_list(1000))

    async def show_student(self, id: str):
        """
        Get the record for a specific student, looked up by `id`.
        """
        if (
            student := await self.collection.find_one({"_id": ObjectId(id)})
        ) is not None:
            return student

        raise HTTPException(status_code=404, detail=f"Student {id} not found")

    async def update_student(self, id: str, student: UpdateStudentModel = Body(...)):
        """
        Update individual fields of an existing student record.

        Only the provided fields will be updated.
        Any missing or `null` fields will be ignored.
        """
        student = {
            k: v for k, v in student.model_dump(by_alias=True).items() if v is not None
        }

        if len(student) >= 1:
            update_result = await self.collection.find_one_and_update(
                {"_id": ObjectId(id)},
                {"$set": student},
                return_document=ReturnDocument.AFTER,
            )
            if update_result is not None:
                return update_result
            else:
                raise HTTPException(status_code=404, detail=f"Student {id} not found")

        # The update is empty, but we should still return the matching document:
        if (existing_student := await self.collection.find_one({"_id": id})) is not None:
            return existing_student

        raise HTTPException(status_code=404, detail=f"Student {id} not found")

    async def delete_student(self, id: str):
        """
        Remove a single student record from the database.
        """
        delete_result = await self.collection.delete_one({"_id": ObjectId(id)})

        if delete_result.deleted_count == 1:
            return Response(status_code=status.HTTP_204_NO_CONTENT)

        raise HTTPException(status_code=404, detail=f"Student {id} not found")


student_repository = StudentCommonRepository()
