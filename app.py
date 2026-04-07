import os
import requests
from flask import Flask, render_template, request, redirect, url_for
from data_manager import DataManager
from models import db, Movie
from dotenv import load_dotenv

app = Flask(__name__)
load_dotenv()

basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data/movies.db')}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

data_manager = DataManager()

OMDB_API_KEY = os.getenv("OMDB_API_KEY")
if not OMDB_API_KEY:
    raise ValueError("OMDB_API_KEY is not set in .env file")


@app.route('/')
def index():
    users = data_manager.get_users()
    return render_template('index.html', users=users)


@app.route('/users', methods=['POST'])
def create_user():
    name = request.form.get('name')
    if name:
        data_manager.create_user(name)
    return redirect(url_for('index'))


@app.route('/users/<int:user_id>/movies', methods=['GET'])
def get_movies(user_id):
    movies = data_manager.get_movies(user_id)
    return render_template('movies.html', movies=movies, user_id=user_id)


@app.route('/users/<int:user_id>/movies', methods=['POST'])
def add_movie(user_id):
    title = request.form.get('title')

    if title:
        url = f"http://www.omdbapi.com/?apikey={OMDB_API_KEY}&t={title}"
        response = requests.get(url)
        data = response.json()

        if data.get("Response") == "True":
            year_value = data.get("Year")
            try:
                year_value = int(year_value[:4]) if year_value else None
            except ValueError:
                year_value = None

            new_movie = Movie(
                name=data.get("Title"),
                director=data.get("Director"),
                year=year_value,
                poster_url=data.get("Poster") if data.get("Poster") != "N/A" else "",
                user_id=user_id
            )
            data_manager.add_movie(new_movie)

    return redirect(url_for('get_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/update', methods=['POST'])
def update_movie(user_id, movie_id):
    new_title = request.form.get('new_title')
    if new_title:
        data_manager.update_movie(movie_id, new_title)
    return redirect(url_for('get_movies', user_id=user_id))


@app.route('/users/<int:user_id>/movies/<int:movie_id>/delete', methods=['POST'])
def delete_movie(user_id, movie_id):
    data_manager.delete_movie(movie_id)
    return redirect(url_for('get_movies', user_id=user_id))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)