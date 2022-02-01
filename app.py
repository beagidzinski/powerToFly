from flask import Flask, jsonify, request
import flask_sqlalchemy
from flask_seeder import FlaskSeeder

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://root:postgres@database:5432/power_to_fly'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = flask_sqlalchemy.SQLAlchemy(app)


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    age = db.Column(db.Integer)
    country = db.Column(db.String(50))

    def __init__(self, id, name, age, country):
        self.id = id
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return f"ID={self.id}, Name={self.name}, Age={self.age}, Country={self.country}"

    def format(self):
        return {
            'name': self.name,
            'age': self.age,
            'country': self.country
        }


seeder = FlaskSeeder()
seeder.init_app(app, db)
db.create_all()
db.session.commit()


@app.route('/users', methods=['GET', 'POST'])
def get_users():
    ROWS_PER_PAGE = 3

    page = request.args.get('page', 1, type=int)
    filters = request.get_json()

    name = None
    age = None
    country = None

    if filters:
        if 'name' in filters:
            name = filters['name']

        if 'age' in filters:
            age_start = filters['age']

        if 'country' in filters:
            country = filters['country']

        users = Users.query.filter(
            Users.name.ilike(name),
            Users.country.ilike(country),
            Users.age.like(age)
        ).paginate(page=page, per_page=ROWS_PER_PAGE)

        users = [{
            'name': user.name,
            'age': user.age,
            'country': user.country
        } for user in users]

        result = jsonify({
            'success': True,
            'users': users,
            'count': len(users)
        })

    else:
        users = Users.query.paginate(page=page, per_page=ROWS_PER_PAGE)
        paginated_users = users.items

        all_users = [{
            'name': user.name,
            'age': user.age,
            'country': user.country
        } for user in paginated_users]

        result = jsonify({
            'success': True,
            'users': all_users,
            'count': len(paginated_users)
        })

    return result
