import unittest
import asynctest
from unittest.mock import MagicMock
from src.schemas.student import StudentModel
from src.controllers.student_repository.common import StudentCommonRepository

class TestStudentCommonRepository(asynctest.TestCase):
    def setUp(self):
        self.collection_mock = asynctest.MagicMock()
        self.repo = StudentCommonRepository(collection_name="test")
        self.repo.collection = self.collection_mock

    async def test_create_document(self):
        # Arrange
        student = StudentModel(name="Test", age=20)
        self.collection_mock.insert_one.return_value = asynctest.MagicMock(inserted_id="123")
        self.collection_mock.find_one.return_value = {"_id": "123", "name": "Test", "age": 20}

        # Act
        result = await self.repo.create_document(student)

        # Assert
        self.collection_mock.insert_one.assert_called_once()
        self.collection_mock.find_one.assert_called_once_with({"_id": "123"})
        self.assertEqual(result, {"_id": "123", "name": "Test", "age": 20})

if __name__ == '__main__':
    asynctest.main()    asynctest.main()