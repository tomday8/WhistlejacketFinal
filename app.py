from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import sqlalchemy as sal
import pandas as pd


app = Flask(__name__)

engine = sal.create_engine('postgresql://127.0.0.1:5432/whistlejacket-randomizer')
conn = engine.connect()



@app.route("/")
def homepage():
    return render_template('index.html')

# @app.route("/movies")
# def movie_recommendation():
#     return render_template('movies.html')


@app.route("/movies")
def movie_recommendation():
    query = "SELECT * FROM movies LIMIT 1"
    result = conn.execute(query)
    df = pd.DataFrame(result.fetchall())
    df.columns = result.keys()
    movie = df.iloc[0].to_dict()
    movie_name = movie['film_name']
    movie_rating = movie['rating']
    return render_template('movies.html', movie_name=movie_name, movie_rating=movie_rating)


