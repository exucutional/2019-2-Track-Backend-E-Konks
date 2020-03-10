import factory
from users.models import User

class RandomUserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Faker('word')
    password = factory.Faker('word')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    email = factory.Faker('email')
