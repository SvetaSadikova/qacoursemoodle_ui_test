from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class LoginMoodle:
    def __init__(self, app):
        self.LogWebdriver = app.MyDriver

    def __password_input(self) -> WebElement:
        return self.LogWebdriver.find_element(By.ID, 'password')

    def __login_input(self) -> WebElement:
        return self.LogWebdriver.find_element(By.ID, 'username')

    def __submit_button(self) -> WebElement:
        return self.LogWebdriver.find_element(By.ID, 'loginbtn')

    def auth_fun(self, login: str, password: str):
        self.__login_input().send_keys(login)
        self.__password_input().send_keys(password)
        self.__submit_button().click()
        print(f'Login is {login}, password is {password}')
