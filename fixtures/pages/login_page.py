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
        self.input_data_method(data_for_login.log, locator_name=(By.ID, 'username'))
        self.input_data_method(data_for_login.passw, locator_name=(By.ID, 'password'))
        if is_submit:
            self.click_method(locator_name=(By.ID, 'loginbtn'), wait_time=3)

    def error_text(self):
        error_text = self.find_element_method(locator_name=(By.ID, 'loginerrormessage'))
        return error_text.text
