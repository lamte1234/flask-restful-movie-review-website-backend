from sqlalchemy.orm import backref
import config
from flask_restful import fields

from models.film_star import film_star, film_star_field
from models.star import star_field
from models.comment import comment_field, UserRating
from models.director import director_field

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
    'director_id': fields.Integer,
    'director': fields.Nested(director_field),
    'stars': fields.List(fields.Nested(star_field)),
    'comments': fields.List(fields.Nested(comment_field))
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

    # relationship
    stars = db.relationship('Star', secondary=film_star, back_populates='films')
    comments = db.relationship('UserRating', backref='user_rating', lazy='select')

    def __repr__(self) -> str:
        return f"Film(film_id={self.film_id})"