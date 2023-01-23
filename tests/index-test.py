import unittest

from app import app

class StatusCodeTestCase(unittest.TestCase):
    def index_content(self):
        tester = app.test_client(self)
        response = tester.get('/playlist')
        self.assertEqual(response.status_code, 500)

    def test_index200(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_movies200(self):
        tester = app.test_client(self)
        response = tester.get('/movies')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
   unittest.main()
