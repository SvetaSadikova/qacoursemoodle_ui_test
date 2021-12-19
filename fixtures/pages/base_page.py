from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, app_moodle):
        self.bp_app = app_moodle

    def find_element_method(self, locator_name, wait_time=10):
        my_element = WebDriverWait(self.bp_app.my_driver, wait_time).until(
            EC.presence_of_element_located(locator_name),
            message=f"Can't find element by locator {locator_name}"
        )
        return my_element

    def click_method(self, locator_name, wait_time=10):
        my_element = self.find_element_method(locator_name, wait_time)
        my_element.click()

    def input_data_method(self, input_data, locator_name, wait_time=10):
        """
        :param input_data: значение, которым будем заполнять input
        :param locator_name: элемент на странице, в который будем вводить значение
        """
        my_element = self.find_element_method(locator_name, wait_time)
        if input_data:
            my_element.send_keys(input_data)
