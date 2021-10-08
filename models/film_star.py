'''
Association object of star and film
'''

import config
from flask_restful import fields

db = config.db

film_star_field = {
    'film_id': fields.Integer,
    'star_id': fields.Integer
}

class FilmStar(db.Model):
    __tablename__ = 'film_star'
    film_id = db.Column(db.Integer, db.ForeignKey('user.username'), primary_key=True)
    star_id = db.Column(db.Integer, db.ForeignKey('film.film_id'), primary_key=True)
    # relationship

    star = db.relationship('Star')

    def __repr__(self) -> str:
        return f"FilmStar(film_id={self.film_id}, star_id={self.star_id})"