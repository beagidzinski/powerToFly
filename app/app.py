from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder
import json

app = Flask(__name__)

alchemy = SQLAlchemy(app)
alchemy.init_app(app)

seeder = FlaskSeeder()
seeder.init_app(app, alchemy)


@app.route('/', methods=['GET'])
def fetch():
    all_users = "Hello World"
    return json.dumps(all_users), 200
