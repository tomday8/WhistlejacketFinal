from flask import Flask, render_template, flash, request, url_for, redirect, session
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm
import sqlalchemy as sal
import pandas as pd
import random
import os

app = Flask(__name__)

engine = sal.create_engine('postgresql://127.0.0.1:5432/whistlejacket-randomizer')
conn = engine.connect()

# AUTHENTICATION TESTING #
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://127.0.0.1:5432/whistlejacket-randomizer"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
SECRET_KEY = os.environ.get('SECRET_KEY') or os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

from models import User
@app.route('/register', methods = ['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(email=form.email.data).first()
        if existing_user:
            flash("An account with this email already exists.")
            return render_template('registration.html', form=form)
        else:
            user = User(firstname =form.firstname.data, email = form.email.data)
            user.set_password(form.password1.data)
            db.session.add(user)
            db.session.commit()
            query = """
                INSERT INTO user_scores
                VALUES ({}, 'Action', 1);

                INSERT INTO user_scores
                VALUES ({}, 'Sci Fi', 1);

                INSERT INTO user_scores
                VALUES ({}, 'Drama', 1);

                INSERT INTO user_scores
                VALUES ({}, 'Animation', 1);

                INSERT INTO user_scores
                VALUES ({}, 'Musical', 1);
                """.format(user.id, user.id, user.id, user.id, user.id)
            conn.execute(query)
            return redirect(url_for('login'))
    return render_template('registration.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    else:
        form = LoginForm()
        if form.validate_on_submit():
            user = User.query.filter_by(email = form.email.data).first()
            if user is not None and user.check_password(form.password.data):
                login_user(user)
                next = request.args.get("next")
                return redirect(next or url_for('home'))
            flash('Invalid email address or Password.')    
        return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/account")
def my_account():
    if current_user.is_authenticated:
        return render_template('account.html')
    else:
        return redirect(url_for('login'))

@app.route("/movies", methods=["GET", "POST"])
def movies():
    if current_user.is_authenticated and len(return_movie(current_user.id)) == 0:
        return render_template('error.html')
    else:    
        if current_user.is_authenticated:
            movie = return_movie(current_user.id)
        else:
            movie = return_movie()
        movie_id = movie['id']
        movie_title = movie['title']
        movie_year = movie['year']
        movie_rating = movie['rating']
        movie_trailer = movie['trailer']
        background_link = "https://www.youtube.com/embed/{}?controls=0&autoplay=1&start=7&mute=1&playinline=1&playlist={}&loop=1".format(movie_trailer, movie_trailer)
        trailer_link = "https://www.youtube.com/embed/{}?autoplay=1&playinline=1&playlist={}&loop=1".format(movie_trailer, movie_trailer)
        return render_template('movies.html', movie_title=movie_title, movie_year=movie_year, movie_rating=movie_rating, movie_trailer=movie_trailer, background_link=background_link, trailer_link=trailer_link, movie_id=movie_id)

@app.route("/trailer", methods=['POST'])
def trailer():
    trailer_id = request.form['trailer_id']
    trailer_link = "https://www.youtube.com/embed/{}?autoplay=1&playinline=1&playlist={}&loop=1".format(trailer_id, trailer_id)
    return render_template('trailer.html', trailer_id=trailer_id, trailer_link=trailer_link)

@app.route('/like', methods=['POST'])
def like():
    user_id = request.form["user_id"]
    movie_id = request.form["movie_id"]
    query = """
        INSERT INTO user_movies (user_id, movie_id, like_dislike) 
        VALUES ({}, {}, 1)
        ON CONFLICT (user_id, movie_id)  DO UPDATE SET like_dislike = 1;
        INSERT INTO user_scores (user_id, genre, score)
        SELECT {}, movies.genre, 1
        FROM movies
        WHERE movies.id = {}
        ON CONFLICT (user_id, genre) DO UPDATE SET score = user_scores.score + 1;
     """.format(user_id, movie_id, user_id, movie_id)
    conn.execute(query)
    return '', 204

@app.route('/dislike', methods=['POST'])
def dislike():
    user_id = request.form["user_id"]
    movie_id = request.form["movie_id"]
    query="""
        INSERT INTO user_movies (user_id, movie_id, like_dislike) 
        VALUES ({}, {}, -1) 
        ON CONFLICT (user_id, movie_id)  
        DO UPDATE SET like_dislike = -1;""".format(user_id, movie_id)
    conn.execute(query)
    return '', 204

@app.route('/neutral', methods=['POST'])
def neutral():
    user_id = request.form["user_id"]
    movie_id = request.form["movie_id"]
    query="""
        INSERT INTO user_movies (user_id, movie_id, like_dislike) 
        VALUES ({}, {}, 0) 
        ON CONFLICT (user_id, movie_id)  
        DO UPDATE SET like_dislike = 0;""".format(user_id, movie_id)
    conn.execute(query)
    return redirect(url_for('likes'))

@app.route('/remove', methods=['POST'])
def remove():
    user_id = request.form["user_id"]
    movie_id = request.form["movie_id"]
    query="""
        UPDATE user_movies 
        SET save_flag = 0 
        WHERE user_id= {} 
        AND movie_id = {}""".format(user_id, movie_id)
    conn.execute(query)
    return redirect(url_for('watchlist'))

@app.route('/save', methods=['POST'])
def save():
    user_id = request.form["user_id"]
    movie_id = request.form["movie_id"]
    query="""
        INSERT INTO user_movies (user_id, movie_id, save_flag) 
        VALUES ({}, {}, 1) 
        ON CONFLICT (user_id, movie_id)  
        DO UPDATE SET save_flag = 1;""".format(user_id, movie_id)
    conn.execute(query)
    return '', 204

@app.route('/deleteAccount', methods=['POST'])
def deleteAccount():
    user_id = request.form["user_id"]
    query="""
        DELETE FROM "user" 
        WHERE id={}""".format(user_id)
    conn.execute(query)
    session.clear()
    return render_template('index.html')

@app.route('/updateName', methods=['POST'])
def updateName():
    user_id = request.form["user_id"]
    firstname = request.form["firstname"]
    query="""
        UPDATE "user" 
        SET firstname = '{}' 
        WHERE id ={}""".format(firstname,user_id)
    conn.execute(query)
    return render_template('account.html')

@app.route('/updateEmail', methods=['POST'])
def updateEmail():
    user_id = request.form["user_id"]
    email = request.form["email"]
    query="""
        UPDATE "user" 
        SET email = '{}' 
        WHERE id ={}""".format(email,user_id)
    conn.execute(query)
    return render_template('account.html')

@app.route('/updatePassword', methods=['POST'])
def updatePassword():
    user = current_user
    user_id = request.form["user_id"]
    password = request.form["password"]
    password_hash = generate_password_hash(password)
    query="""
        UPDATE "user" 
        SET password_hash = '{}' 
        WHERE id ={}""".format(password_hash,user_id)
    conn.execute(query)
    return render_template('account.html')

@app.route('/watch-list')
def watchlist():
    if current_user.is_authenticated:
        saved_movies = get_saves(current_user.id)
        return render_template('watchlist.html', saved_movies=saved_movies)
    else:
        return redirect(url_for('home'))

@app.route('/likes')
def likes():
    if current_user.is_authenticated:
        liked_movies = get_likes(current_user.id)
        disliked_movies = get_dislikes(current_user.id)
        return render_template('likes.html', liked_movies=liked_movies, disliked_movies=disliked_movies)
    else:
        return redirect(url_for('home'))

def return_movie(user_id=None):
    if current_user.is_authenticated:
        query = """
            SELECT movies.*, user_scores.score
            FROM movies
            LEFT JOIN user_scores
            ON user_scores.genre = movies.genre
            AND user_scores.user_id = {}
            WHERE movies.id 
            NOT IN (SELECT movie_id 
            FROM user_movies 
            WHERE user_id = {} 
            AND like_dislike = -1)
            """.format(user_id, user_id)
        result = conn.execute(query)
        df = pd.DataFrame(result.fetchall())
        if len(df.columns) == 0:
            query = """
                SELECT * FROM movies"""
            result = conn.execute(query)
            df = pd.DataFrame(result.fetchall())
            df.columns = result.keys()
            movie = random.choice(df.to_dict("records"))
            return movie
        df.columns = result.keys()
        total_score = df["score"].sum()
        if total_score == 0:
            query = """
                SELECT * FROM movies"""
            result = conn.execute(query)
            df = pd.DataFrame(result.fetchall())
            df.columns = result.keys()
            movie = random.choice(df.to_dict("records"))
            return movie
        df['likelihood'] = df['score'] / total_score
        df = df.sample(weights=df['likelihood'], n=1)
        movie = df.to_dict(orient='records')[0]
        return movie
    else:
        query = """
            SELECT * FROM movies"""
        result = conn.execute(query)
        df = pd.DataFrame(result.fetchall())
        df.columns = result.keys()
        movie = random.choice(df.to_dict("records"))
        return movie

def return_movie_trailer(id):
    query = """
        SELECT trailer 
        FROM movies 
        WHERE id ={}""".format(id)
    result = conn.execute(query)
    df = pd.DataFrame(result.fetchall())
    df.columns = result.keys()
    movie_trailer = df['trailer'].values[0]
    return movie_trailer

def get_likes(user_id):
    query = """
        SELECT * 
        FROM movies 
        WHERE id 
        IN (SELECT movie_id FROM user_movies WHERE user_id = {} AND like_dislike = 1)""".format(user_id)
    result = conn.execute(query)
    df = pd.DataFrame(result.fetchall())
    if len(df.columns) == 0:
        return []
    df.columns = result.keys()
    return df.to_dict("records")

def get_saves(user_id):
    query = """
        SELECT * 
        FROM movies 
        WHERE id 
        IN (SELECT movie_id FROM user_movies WHERE user_id = {} AND save_flag = 1)""".format(user_id)
    result = conn.execute(query)
    df = pd.DataFrame(result.fetchall())
    if len(df.columns) == 0:
        return []
    df.columns = result.keys()
    return df.to_dict("records")

def get_dislikes(user_id):
    query = """
        SELECT * 
        FROM movies 
        WHERE id 
        IN (SELECT movie_id FROM user_movies WHERE user_id = {} AND like_dislike = -1)""".format(user_id)
    result = conn.execute(query)
    df = pd.DataFrame(result.fetchall())
    if len(df.columns) == 0:
        return []
    df.columns = result.keys()
    return df.to_dict("records")
