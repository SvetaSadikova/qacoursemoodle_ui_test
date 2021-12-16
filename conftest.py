import pytest as pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from fixtures.pages.app_moodle import ApplicationMoodle


@pytest.fixture() # TODO add (scope='session')
def app_moodle(request):
    url = request.config.getoption("--base_moodle_url")
    driver = webdriver.Chrome(ChromeDriverManager().install())
    moodle = ApplicationMoodle(driver, url)
    yield moodle
    moodle.quit()


def pytest_addoption(parser):
    parser.addoption("--base_moodle_url", action="store", default="https://qacoursemoodle.innopolis.university/login/index.php", help="Moodle url")





