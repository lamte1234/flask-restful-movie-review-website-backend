import config
from flask_restful import fields

db = config.db

film_field = {
    'film_id': fields.Integer,
    'title': fields.String,
    'certificate': fields.String,
    'release_year': fields.String,
    'length': fields.String,
    'description': fields.String,
    'rating': fields.String,
    'poster_url': fields.String,
    'trailer_url': fields.String,
    'director_id': fields.Integer
}

class Film(db.Model):
    __tablename__ = 'film'
    film_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    certificate = db.Column(db.String(10), nullable=False)
    release_year = db.Column(db.String(10), nullable=False)
    length = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(300), nullable=False)
    rating = db.Column(db.String(200), nullable=False)
    poster_url = db.Column(db.String(200), nullable=True)
    trailer_url = db.Column(db.String(200), nullable=True)
    director_id = db.Column(db.Integer, db.ForeignKey('director.director_id'))

    def __repr__(self) -> str:
        return f"Film(film_id={self.film_id})"