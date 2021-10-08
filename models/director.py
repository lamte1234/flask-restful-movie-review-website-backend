import config
from flask_restful import fields


db = config.db

director_field = {
    'director_id': fields.Integer,
    'name': fields.String
}

class Director(db.Model):
    __tablename__ = 'director'
    director_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    films = db.relationship('Film', backref='director', lazy='select')

    def __repr__(self) -> str:
        return f"Director(director_id={self.director_id})"