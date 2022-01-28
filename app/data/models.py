import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()


def get_all(model):
    data = model.query.all()
    return data


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    country = db.Column(db.String(50))