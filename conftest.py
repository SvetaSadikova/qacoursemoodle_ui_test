import logging

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from fixtures.models.fake_data import LoginData, RegistrationData
from fixtures.pages.app_moodle import ApplicationMoodle

moodle_logger = logging.getLogger('moodle')


# TODO add (scope='session')
@pytest.fixture(scope='session')
def data_for_login(request):
    userlogin = request.config.getoption('--base_username')
    userPassword = request.config.getoption('--base_password')
    return LoginData(userlogin, userPassword)


@pytest.fixture(scope='session')
def data_for_register(request):
    userlogin = request.config.getoption('--base_username')
    userPassword = request.config.getoption('--base_password')
    return RegistrationData(userlogin, userPassword)


@pytest.fixture()
def app_moodle(request):
    # url
    url = request.config.getoption("--base_moodle_url")
    headless = request.config.getoption("--headless_option")

    # Опции драйвера
    chrome_options = Options()
    chrome_options.headless = headless  # не работает, даже если указать true ???

    # Драйвер
    driver = webdriver.Chrome(ChromeDriverManager().install())
    moodle_logger.info(f'Open browser with URL {url}')

    moodle = ApplicationMoodle(driver, url)
    yield moodle
    moodle.quit()
    moodle_logger.info(f'End session. Close browser')


def pytest_addoption(parser):
    parser.addoption("--base_username", action="store", default="super_qa_2021", help="Moodle username"),
    parser.addoption("--base_password", action="store", default="password11!", help="Moodle password"),
    parser.addoption("--base_moodle_url", action="store",
                     default="https://qacoursemoodle.innopolis.university", help="Moodle url"),
    parser.addoption("--headless_option", action="store",
                     default="false", help="Moodle url")
