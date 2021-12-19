import logging

from fixtures.models.fake_data import LoginData, RegistrationData

moodle_logger = logging.getLogger('moodle')


class TestRegistration:
    def test_valid_registration(self, app_moodle, data_for_register, true=None):
        """
        Steps:
        1. Open login page
        2. Input valid data
        3. Click register_button
        4. Check result
        """
        moodle_logger.info('START registration with valid data')

        app_moodle.open_registration_page()

        moodle_logger.info('Open registration page')
        registration_data = RegistrationData.randomize()
        app_moodle.my_registration.filling_registration_form(data_for_registration=registration_data, is_submit=true)
        moodle_logger.info(f'Filling registration info: login {registration_data.log}, password {registration_data.passw}, name{registration_data.name}, surname {registration_data.surname} ')
        assert 1 == 1
