from fixtures.models.login_data import LoginData


class TestLogin:
    def test_login_with_valid_data(self, app_moodle):
        """
        Steps:
        1. Open login page
        2. Auth with valid data
        3. Check result
        """
        app_moodle.open_login_page()
        login_data = LoginData(login='super_qa_2021', password='password11')
        app_moodle.MyLogin.auth_fun(login_data)
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



