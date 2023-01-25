import unittest
from app import app, return_movie, conn
import subprocess
from unittest.mock import MagicMock

# Run tests: python3 -m unittest discover -s tests/

class ContentOfMovies(unittest.TestCase):
    def test_movies_body(self):
        tester = app.test_client(self)
        response = tester.get('/movies', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'<div class="content">' in response.data)

    def test_return_movie(self):
        movie = return_movie()
        self.assertIn("id", movie)
        self.assertIn("title", movie)
        self.assertIn("rating", movie)
        self.assertIn("year", movie)

if __name__ == "__main__":
   unittest.main()
