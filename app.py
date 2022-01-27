import json

from . import create_app
from data.database import db
from data.models import Users

app = create_app()

@app.route('/', methods=['GET'])
def fetch():
    users = db.get_all(Users)
    all_users = []
    for user in users:
        new_user = {
            "id": user.id,
            "name": user.name,
            "country": user.country,
            "age": user.age
        }

        all_users.append(new_user)
    return json.dumps(all_users), 200