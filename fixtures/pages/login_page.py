from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from fixtures.models.fake_data import LoginData
from fixtures.pages.base_page import BasePage


class LoginMoodle(BasePage):

    def __password_input(self) -> WebElement:
        return self.find_element_method(locator_name=(By.ID, 'password'), wait_time=3)

    def __login_input(self) -> WebElement:
        return self.find_element_method(locator_name=(By.ID, 'username'))

    def __submit_button(self) -> WebElement:
        return self.find_element_method(locator_name=(By.ID, 'loginbtn'))

    def auth_fun(self, data_for_login: LoginData, is_submit: bool = True):
        """
        Функция авторизации
        TODO Добавить проверку на is_login
        """
        self.__login_input().send_keys(data_for_login.log)
        self.__password_input().send_keys(data_for_login.passw)
        if is_submit:
            self.__submit_button().click()

    def error_text(self):
        error_text = self.find_element_method(locator_name=(By.ID, 'loginerrormessage'))
        return error_text.text
