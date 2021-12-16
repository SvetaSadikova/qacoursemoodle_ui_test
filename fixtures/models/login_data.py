from faker import Faker

fake = Faker('Ru-ru')


class LoginData:
    def __init__(self, login=None, password=None):
        self.log = login
        self.passw = password

    @staticmethod
    def randomize():
        return LoginData(login=fake.email(), password=Faker().password())
