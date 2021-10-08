import config
from flask_restful import fields

db = config.db

user_field = {
    'username': fields.String,
    'password': fields.String
}

class User(db.Model):
    __tablename__ = ''
    username = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"Username(username={self.username})"