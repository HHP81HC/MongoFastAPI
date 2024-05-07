import asynctest
from src.schemas.student import StudentModel
from src.controllers.student_repository.common import StudentCommonRepository


class TestStudentCommonRepository(asynctest.TestCase):
    def setUp(self):
        self.collection_mock = asynctest.MagicMock()
        self.repo = StudentCommonRepository(collection_name="test")
        self.repo.collection = self.collection_mock

    def tearDown(self) -> None:
        self.collection_mock.reset_mock()

    async def test_create_document(self):
        # Arrange
        excepted_data = {
            "_id": "123",
            "name": "Test",
            "email": "test@gmail.com",
            "course": "Python",
            "gpa": 20
        }
        student = StudentModel(name="Test", email="test@gmail.com", course="Python", gpa=20)
        self.collection_mock.insert_one.return_value = asynctest.MagicMock(inserted_id="123")
        self.collection_mock.find_one.return_value = excepted_data

        # Act
        result = await self.repo.create_document(student)

        # Assert
        self.collection_mock.insert_one.assert_called_once()
        self.collection_mock.find_one.assert_called_once_with({"_id": "123"})
        self.assertEqual(result, excepted_data)


if __name__ == '__main__':
    asynctest.main()
