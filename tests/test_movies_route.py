import unittest
from app import app, return_movie, conn
import subprocess
from unittest.mock import MagicMock

class ContentOfMovies(unittest.TestCase):
    def test_movies_body(self):
        tester = app.test_client(self)
        response = tester.get('/movies', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(b'<h1>movies</h1>' in response.data)

    def test_return_movie(self):
        movie = return_movie()
        self.assertIn("id", movie)
        self.assertIn("title", movie)
        self.assertIn("rating", movie)

if __name__ == "__main__":
   unittest.main()



# import psycopg2

# def reset_movies_table():
#     with open('../seeds/movies_seeds.sql', 'r') as seed_file:
#         seed_sql = seed_file.read()
#     connection = psycopg2.connect(host='127.0.0.1', dbname='whistlejacket-randomizer')
#     cursor = connection.cursor()
#     cursor.execute(seed_sql)
#     connection.commit()
#     cursor.close()
#     connection.close()

# class TestExample(unittest.TestCase):
#     def setUp(self):
#         reset_movies_table()