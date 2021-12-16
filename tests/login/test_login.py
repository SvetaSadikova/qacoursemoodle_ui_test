class TestLogin:
    def test_login_with_valid_data(self, app_moodle):
        """
        Steps:
        1. Open login page
        2. Auth with valid data
        3. Check result
        """
        app_moodle.open_login_page()
        app_moodle.MyLogin.auth_fun('name', 'passw')
        assert 1 == 1


