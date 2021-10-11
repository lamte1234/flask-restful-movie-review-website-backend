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

film_star = db.Table(
    "film_star",
    db.Column("star_id", db.Integer, db.ForeignKey("star.star_id")),
    db.Column("film_id", db.Integer, db.ForeignKey("film.film_id")),
)