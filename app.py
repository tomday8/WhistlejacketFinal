from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import sqlalchemy as sal
import pandas as pd
import random


app = Flask(__name__)

engine = sal.create_engine('postgresql://127.0.0.1:5432/whistlejacket-randomizer')
conn = engine.connect()



@app.route("/")
def homepage():
    return render_template('index.html')


@app.route("/movies")
def movie_recommendation():
    movie = return_movie()
    movie_title = movie['title']
    movie_rating = movie['rating']
    return render_template('movies.html', movie_title=movie_title, movie_rating=movie_rating)

def return_movie():
    query = "SELECT * FROM movies"
    result = conn.execute(query)
    df = pd.DataFrame(result.fetchall())
    df.columns = result.keys()
    movie = random.choice(df.to_dict("records"))
    return movie