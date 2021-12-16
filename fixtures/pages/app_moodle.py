from fixtures.pages.login_page import LoginMoodle
from fixtures.pages.registration_page import RegistrationPage


class ApplicationMoodle:
    def __init__(self, driver, url):
        self.MyDriver = driver
        self.MyUrl = url
        self.MyLogin = LoginMoodle(self)
        self.MyRegistration = RegistrationPage(self)

    def quit(self):
        self.MyDriver.quit()

    def open_login_page(self):
        #   self.MyDriver.get(self.MyUrl)
        link = self.MyUrl + '/login/index.php'
        self.MyDriver.get(link)

    def open_registration_page(self):
        """
        тут надо придумать как передавать адрес конкретной страницы.
        Как варинт в фикстуру app_moodle в --base_moodle_url в качестве дефолтного передать главную страницу
        https://qacoursemoodle.innopolis.university/
        а в методе добавлять к нему абсолютные пути
        """
        link = self.MyUrl + '/login/signup.php'
        self.MyDriver.get(link)
