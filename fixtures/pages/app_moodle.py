from fixtures.pages.login_f import LoginMoodle


class ApplicationMoodle:
    def __init__(self, driver, url):
        self.MyDriver = driver
        self.MyUrl = url
        self.MyLogin = LoginMoodle(self)
    #    self.Registration = RegistrationPage(self)

    def quit(self):
        self.MyDriver.quit()

    def open_login_page(self):
        self.MyDriver.get(self.MyUrl)
