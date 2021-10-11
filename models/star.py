import config
from flask_restful import fields

from models.film_star import film_star

db = config.db

star_field = {
    'star_id': fields.Integer,
    'name': fields.String
}

class Star(db.Model):
    __tablename__ = 'star'
    star_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    # relationship

    films = db.relationship('Film', secondary=film_star, back_populates='stars')

    def __repr__(self) -> str:
        return f"Star(director_id={self.star_id})"