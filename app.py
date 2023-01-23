from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route("/movies")
def movie_rec():
    return render_template('movies.html')
