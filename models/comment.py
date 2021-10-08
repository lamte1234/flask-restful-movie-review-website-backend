'''
Association object of user and film
'''

import config
from flask_restful import fields

db = config.db

comment_field = {
    'username': fields.String,
    'rating': fields.String,
    'film_id': fields.Integer
}

class Comment(db.Model):
    __tablename__ = 'user_rating'
    username = db.Column(db.String(100), db.ForeignKey('user.username'), primary_key=True)
    rating = db.Column(db.String(200), nullable=False)
    film_id = db.Column(db.Integer, db.ForeignKey('film.film_id'), primary_key=True)

    def __repr__(self) -> str:
        return f"Comment(username={self.username})"