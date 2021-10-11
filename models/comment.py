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



class UserRating(db.Model):
    __tablename__ = 'user_rating'
    username = db.Column("username", db.String(100), db.ForeignKey("user.username"), primary_key=True)
    film_id = db.Column("film_id", db.Integer, db.ForeignKey("film.film_id"), primary_key=True)
    rating = db.Column('rating', db.String(200), nullable=False)


    def __repr__(self) -> str:
        return f'Comment(film_id={self.film_id}, username={self.username})'