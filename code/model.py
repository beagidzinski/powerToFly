import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'cats'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    surname = db.Column(db.String(100))
    gender = db.Column(db.String(100))