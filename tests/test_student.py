import unittest
from fastapi.testclient import TestClient
from app import app  # Assuming your FastAPI app is named 'app'


class TestStudentAPI(unittest.TestCase):
    def setUp(self):
        self.client = TestClient(app)

    def tearDown(self):
        # Clean up any test data if necessary
        pass

    def test_create_student(self):
        # Test creating a new student
        data = {
            "name": "Jane Doe",
            "email": "jdoe@example.com",
            "course": "Experiments, Science, and Fashion in Nanophotonics",
            "gpa": 3.0,
        }
        response = self.client.post("/api/students", json=data)
        self.assertEqual(response.status_code, 201)
        created_student = response.json()

        # Assert the created student matches the input data or whatever criteria you have
        self.assertEqual(created_student['name'], data['name'])
        self.assertEqual(created_student['email'], data['email'])
        self.assertEqual(created_student['course'], data['course'])
        self.assertEqual(created_student['gpa'], data['gpa'])

    def test_list_students(self):
        # Create a new student to list
        data = {
            "name": "Jane Doe",
            "email": "jdoe@example.com",
            "course": "Experiments, Science, and Fashion in Nanophotonics",
            "gpa": 3.0,
        }
        self.client.post("/api/students", json=data)

        # Test listing all students
        response = self.client.get("/api/students")
        self.assertEqual(response.status_code, 200)
        students = response.json()['students']
        self.assertGreater(len(students), 0)




if __name__ == "__main__":
    unittest.main()
