import unittest

from app import app

class StatusCodeTestCase(unittest.TestCase):
    def test_index_200(self):
        tester = app.test_client(self)
        response = tester.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_movies_200(self):
        tester = app.test_client(self)
        response = tester.get('/movies')
        self.assertEqual(response.status_code, 200)
    
    def test_non_existent_route(self):
        tester = app.test_client(self)
        response = tester.get('/playlist')
        self.assertEqual(response.status_code, 404)

if __name__ == "__main__":
   unittest.main()