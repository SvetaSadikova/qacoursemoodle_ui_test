from fixtures.pages.login_page import LoginMoodle
from fixtures.pages.registration_page import RegistrationPage


class ApplicationMoodle:
    def __init__(self, driver, url):
        self.my_driver = driver
        self.my_url = url
        self.my_login = LoginMoodle(self)
        self.my_registration = RegistrationPage(self)

    def quit(self):
        self.my_driver.quit()

    def open_login_page(self):
        #   self.my_driver.get(self.my_url)
        link = self.my_url + '/login/index.php'
        self.my_driver.get(link)

    def open_registration_page(self):
        """
        тут надо придумать как передавать адрес конкретной страницы.
        Как варинт в фикстуру app_moodle в --base_moodle_url в качестве дефолтного передать главную страницу
        https://qacoursemoodle.innopolis.university/
        а в методе добавлять к нему абсолютные пути
        """
        link = self.my_url + '/login/signup.php'
        self.my_driver.get(link)
