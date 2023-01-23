import unittest

from app import app

class ContentOfMovies(unittest.TestCase):
    def test_movies_body(self):
        tester = app.test_client(self)
        response = tester.get('/movies', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'<h1>movies</h1>' in response.data)

if __name__ == "__main__":
   unittest.main()
