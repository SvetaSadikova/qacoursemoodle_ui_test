from faker import Faker

fake = Faker('Ru-ru')


class LoginData:
    def __init__(self, login=None, password=None):
        self.log = login
        self.passw = password

    @staticmethod
    def randomize():
        return LoginData(login=fake.email(), password=Faker().password())


class RegistrationData:
    def __init__(self, login=None, password=None, email=None, firstname=None, lastname=None, city=None):
        self.log = login
        self.passw = password
        self.mail = email
        self.name = firstname
        self.surname = lastname
        self.city = city


    @staticmethod
    def randomize():
        return RegistrationData(login=fake.email(), password=fake.password(), firstname=fake.name(), lastname=fake.surname()) # TODO дописать остальные атрибуты