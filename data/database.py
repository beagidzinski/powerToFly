from .models import db


def get_all(model):
    data = model.query.all()
    return data

def commit_changes():
    db.session.commit()