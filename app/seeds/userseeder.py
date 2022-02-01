from flask_seeder import Seeder, Faker, generator
from app.services.models import Base


class Country(generator):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._lines = None

    def generate(self):
        if self._lines is None:
            self._lines = generator.read_resource('countries.txt')

        country = self.rnd.choice(self._lines)

        return country


class Users(Base):
    def __init__(self, id_num=None, name=None, age=None, country=None):
        self.id_num = id_num
        self.name = name
        self.age = age
        self.country = country

    def __str__(self):
        return "ID=%d, Name=%s, Age=%d, Country=%s" % (self.id_num, self.name, self.age, self.country)


class UserSeeder(Seeder):
    def __init__(self, db=None):
        super().__init__(db=db)
        self.priority = 10

    def run(self):
        countries = Country()

        faker = Faker(
            cls=Users,
            init={
                "id_num": generator.Sequence(),
                "name": generator.Name(),
                "age": generator.Integer(start=20, end=100),
                "country": countries.generate()
            }
        )

        for user in faker.create(5):
            print("Adding user: %s" % user)
            self.db.session.add(user)
