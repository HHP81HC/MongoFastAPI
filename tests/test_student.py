import asynctest
from src.schemas.student import StudentModel
from src.controllers.student_repository.common import StudentCommonRepository


class TestStudentCommonRepository(asynctest.TestCase):
    def setUp(self):
        self.collection_mock = asynctest.MagicMock()
        self.repo = StudentCommonRepository(collection_name="test")
        self.repo.collection = self.collection_mock

        # Mock the insert_one and find_one methods with CoroutineMock
        self.collection_mock.insert_one = asynctest.CoroutineMock()
        self.collection_mock.find_one = asynctest.CoroutineMock()

    def tearDown(self) -> None:
        self.collection_mock.insert_one.reset_mock()
        self.collection_mock.find_one.reset_mock()

    async def test_create_document(self):
        # Arrange
        excepted_data = {
            "_id": "123",
            "name": "Jane Doe",
            "email": "jdoe@example.com",
            "course": "Experiments, Science, and Fashion in Nanophotonics",
            "gpa": 3.0,
        }
        student = StudentModel(
            name="Jane Doe",
            email="jdoe@example.com",
            course="Experiments, Science, and Fashion in Nanophotonics",
            gpa=3.0
        )
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
