# Standard Library
import asyncio
import unittest

from ..app import app

# Third Party
from fastapi.testclient import TestClient


# Create a test client using FastAPI's TestClient
client = TestClient(app)


class TestStudentEndpoints(unittest.TestCase):
    def setUp(self):
        self.loop = asyncio.get_event_loop()
        self.sample_student = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "course": "Computer Science",
            "gpa": 3.5,
        }

    def tearDown(self):
        pass

    def test_create_student(self):
        """
        Test creating a new student.
        """
        response = client.post("/students/", json=self.sample_student)
        self.assertEqual(response.status_code, 201)
        self.assertIn("id", response.json())
        created_student = response.json()
        self.assertEqual(created_student["name"], self.sample_student["name"])
        self.assertEqual(created_student["email"], self.sample_student["email"])
        self.assertEqual(created_student["course"], self.sample_student["course"])


# Run the tests
if __name__ == "__main__":
    unittest.main()
