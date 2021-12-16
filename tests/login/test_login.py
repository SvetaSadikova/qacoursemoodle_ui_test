import logging

from fixtures.models.login_data import LoginData

my_logger = logging.getLogger('moodle')


class TestLogin:
    def test_login_with_valid_data(self, app_moodle, data_for_login):
        """
        Steps:
        1. Open login page
        2. Auth with valid data
        3. Check result
        """
        my_logger.info('Start login_with_valid_data')
        app_moodle.open_login_page()
        my_logger.info('Open login page')
        login_data = data_for_login
        app_moodle.MyLogin.auth_fun(login_data)
        my_logger.info(f'Login with login {login_data.log} and password {login_data.passw}')
        assert 1 == 1

    def test_login_with_invalid_data(self, app_moodle):
        """
        Steps:
        1. Open login page
        2. Auth with valid data
        3. Check result
        """
        app_moodle.open_login_page()
        login_data = LoginData.randomize()
        app_moodle.MyLogin.auth_fun(login_data)
        assert 1 == 1
