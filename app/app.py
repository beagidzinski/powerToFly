from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder
import json

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://root:postgres@database:5432/power_to_fly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    country = db.Column(db.String(50))


db.create_all()
db.session.commit()

seeder = FlaskSeeder()
seeder.init_app(app, db)


@app.route('/', methods=['GET'])
def fetch():
    all_users = "Hello World"
    return json.dumps(all_users), 200
