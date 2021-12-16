from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement

from fixtures.models.fake_data import RegistrationData
from fixtures.pages.base_page import BasePage


class RegistrationPage(BasePage):
    def filling_registration_form(self, data_for_registration: RegistrationData):
        pass
    """
    создать каждый импут через find_element_method().
    создать элемент "кнопка" через find_element_method().    
    заполнить импут данными через фэйкер (!! - фэйковый email положить сначала с переменную, чтобы заполнить одинаковым значением два поля).Использовать кастомный send_keys()
    вызвать клик по элементу кнопка. Использовать кастомный click()
    """

