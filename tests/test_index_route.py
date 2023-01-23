import unittest

from app import app

class ContentOfIndex(unittest.TestCase):
    def test_index_body(self):
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'<h1>Welcome to the movie randomizer</h1>' in response.data)

if __name__ == "__main__":
   unittest.main()
