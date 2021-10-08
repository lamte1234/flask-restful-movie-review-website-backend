import config
from flask_restful import fields

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

    film_star = db.relationship('FilmStar')

    def __repr__(self) -> str:
        return f"Star(director_id={self.star_id})"