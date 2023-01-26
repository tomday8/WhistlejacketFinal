import unittest
from app import app
import psycopg2

# Run tests: python3 -m unittest discover -s tests/

def reset_movies_table():
    with open('../seeds/movies_seeds.sql', 'r') as seed_file:
        seed_sql = seed_file.read()
    connection = psycopg2.connect(host='127.0.0.1', dbname='whistlejacket-randomizer')
    cursor = connection.cursor()
    cursor.execute(seed_sql)
    connection.commit()
    cursor.close()
    connection.close()

class TestExample(unittest.TestCase):
    def setUp(self):
        reset_movies_table()

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