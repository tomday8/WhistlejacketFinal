import unittest
from app import app

# Run tests: python3 -m unittest discover -s tests/

class ContentOfIndex(unittest.TestCase):
    def test_index_body(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'<h1>Welcome to The Movie Randomizer</h1>' in response.data)

if __name__ == "__main__":
   unittest.main()
