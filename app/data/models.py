import flask_sqlalchemy
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
db = flask_sqlalchemy.SQLAlchemy()


def get_all(model):
    data = model.query.all()
    return data


class Users(Base):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    country = db.Column(db.String(50))