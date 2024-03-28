import unittest
from app import app  # Assuming 'app' is the Flask application
import json

class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_read_route(self):
        # Make a GET request to the read route
        response = self.app.get('/books')

        # Check if the response status code is 200 OK
        self.assertEqual(response.status_code, 200)

        # Convert response data from JSON to dictionary
        data = json.loads(response.data)

        # Assuming the response contains a list of books
        self.assertIsInstance(data, list)

        # Add more assertions as needed to verify the response data
