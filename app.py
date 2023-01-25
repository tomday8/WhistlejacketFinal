from flask import Flask, render_template, flash, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import sqlalchemy as sal
import pandas as pd
import random
import os
from flask_login import LoginManager, UserMixin, login_user, current_user, logout_user
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from forms import RegistrationForm, LoginForm


app = Flask(__name__)

engine = sal.create_engine('postgresql://127.0.0.1:5432/whistlejacket-randomizer')
conn = engine.connect()


# AUTHENTICATION TESTING #
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://127.0.0.1:5432/whistlejacket-randomizer"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

class User(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(50), index=True, unique=True)
  email = db.Column(db.String(150), unique = True, index = True)
  password_hash = db.Column(db.String(150))
  joined_at = db.Column(db.DateTime(), default = datetime.utcnow, index = True)

  def set_password(self, password):
        self.password_hash = generate_password_hash(password)

  def check_password(self,password):
      return check_password_hash(self.password_hash,password)



@app.route('/register', methods = ['POST','GET'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        existing_user = User.query.filter_by(username=form.username.data).first()
        if existing_user:
            form.username.errors.append("Username already taken.")
            return render_template('registration.html', form=form)
        else:
            user = User(username =form.username.data, email = form.email.data)
            user.set_password(form.password1.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('login'))
    return render_template('registration.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():

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
# @login_required
def logout():
    logout_user()
    return redirect(url_for('home'))
########


@app.route("/home")
def home():
    return render_template('index.html')


@app.route("/movies")
def movie_recommendation():
    movie = return_movie()
    movie_title = movie['title']
    movie_year = movie['year']
    movie_rating = movie['rating']
    movie_trailer=movie['trailer']
    trailer_link = "https://www.youtube.com/embed/{}?&autoplay=1&start=6&mute=1&playinline=1&playlist={}&loop=1".format(movie_trailer, movie_trailer)
    return render_template('movies.html', movie_title=movie_title, movie_year=movie_year, movie_rating=movie_rating, trailer_link=trailer_link)

@app.route("/movies_demo")
def movies_demo():
    movie_trailer=movie['trailer']
    return_movie_trailer()
    return render_template('movies_demo.html')


def return_movie():
    query = "SELECT * FROM movies"
    result = conn.execute(query)
    df = pd.DataFrame(result.fetchall())
    df.columns = result.keys()
    movie = random.choice(df.to_dict("records"))
    return movie

def return_movie_trailer(id):
    query = "SELECT trailer FROM movies WHERE id ={}".format(id)
    result = conn.execute(query)
    df = pd.DataFrame(result.fetchall())
    df.columns = result.keys()
    movie_trailer = df['trailer'].values[0]
    return movie_trailer