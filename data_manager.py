from models import db, User, Movie
from sqlalchemy.exc import SQLAlchemyError


class DataManager:
    """Handles all database operations for users and movies."""

    def create_user(self, name):
        """Creates a new user."""
        try:
            new_user = User(name=name)
            db.session.add(new_user)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()

    def get_users(self):
        """Returns all users."""
        return User.query.all()

    def get_movies(self, user_id):
        """Returns all movies for a specific user."""
        return Movie.query.filter_by(user_id=user_id).all()

    def add_movie(self, movie):
        """Adds a new movie to the database."""
        try:
            db.session.add(movie)
            db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()

    def update_movie(self, movie_id, new_title):
        """Updates the title of a movie."""
        try:
            movie = db.session.get(Movie, movie_id)
            if movie:
                movie.name = new_title
                db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()

    def delete_movie(self, movie_id):
        """Deletes a movie."""
        try:
            movie = db.session.get(Movie, movie_id)
            if movie:
                db.session.delete(movie)
                db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()

    def delete_user(self, user_id):
        """Deletes a user and all associated movies."""
        try:
            user = db.session.get(User, user_id)
            if user:
                Movie.query.filter_by(user_id=user_id).delete()
                db.session.delete(user)
                db.session.commit()
        except SQLAlchemyError:
            db.session.rollback()
