import logging

from fixtures.models.fake_data import LoginData

moodle_logger = logging.getLogger('moodle')


class TestLogin:
    def test_login_with_valid_data(self, app_moodle, data_for_login, true=None):
        """
        Steps:
        1. Open login page
        2. Auth with valid data
        3. Check result
        """
        moodle_logger.info('Start login_with_valid_data')
        app_moodle.open_login_page()
        moodle_logger.info('Open login page')
        login_data = data_for_login
        app_moodle.my_login.auth_fun(data_for_login=login_data, is_submit=true)
        moodle_logger.info(f'Login with login {login_data.log} and password {login_data.passw}')
        assert 1 == 1

    def test_login_with_invalid_data(self, app_moodle):
        """
        Steps:
        1. Open login page
        2. Auth with invalid data
        3. Check result
        """
        app_moodle.open_login_page()
        login_data = LoginData.randomize()
        app_moodle.my_login.auth_fun(login_data)
        assert app_moodle.my_login.error_text() == 'Неверный логин или пароль, попробуйте заново.'
