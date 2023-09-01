"""
Module Description: Test cases for the Login Page.

This module contains test cases to validate the functionality of the Login Page.
"""

# Standard library
import time

# Third-party
import pytest
from selenium import webdriver

# First-party
from pageObjects.loginPage import Login


@pytest.fixture()
def setup():
    """
    Fixture to set up the WebDriver instance before running each test case.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestLogin:
    """
    Test class for validating the Login Page.
    """
    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    VALID_USERNAME = "Admin"
    VALID_PASSWORD = "admin123"
    INVALID_USERNAME = "InvalidUser"
    INVALID_PASSWORD = "invalidpass"
    INVALID_CREDS_ALERT = "Invalid credentials"
    HOME_PAGE = "dashboard"
    REQUIRED_FIELD = ["Mandatory", "Required", "Obligatorio"]

    def test_valid_login(self, setup):
        """
        Test successful login with valid credentials.
        """
        self.driver = setup
        self.driver.get(self.url)
        login_object = Login(self.driver)
        assert login_object.is_login_form_displayed()
        login_object.enter_username(self.VALID_USERNAME)
        login_object.enter_password(self.VALID_PASSWORD)
        login_object.click_login()
        assert self.HOME_PAGE in self.driver.current_url
        time.sleep(3)

    def test_logout(self, setup):
        """
        Test successful logout after logging in.
        """
        self.driver = setup
        self.driver.get(self.url)

        login_object = Login(self.driver)
        assert login_object.is_login_form_displayed()

        login_object.enter_username(self.VALID_USERNAME)
        login_object.enter_password(self.VALID_PASSWORD)
        login_object.click_login()
        # Assert successful login
        assert self.HOME_PAGE in self.driver.current_url
        time.sleep(3)

        # Perform logout and assert successful logout
        login_object.view_drop_down_menu()
        login_object.click_logout()
        assert login_object.is_login_form_displayed()
        time.sleep(3)

    def test_password_reset_request(self, setup):
        """
        Test requesting a password reset.
        """
        self.driver = setup
        self.driver.get(self.url)
        login_object = Login(self.driver)
        login_object.click_forgot_password_link()
        login_object.enter_username(self.VALID_USERNAME)
        login_object.click_reset_password_button()
        # Assert successful password reset request
        assert login_object.check_reset_link_sent_message()

    def test_invalid_username(self, setup):
        """
        Test login with an invalid username.
        """
        self.driver = setup
        self.driver.get(self.url)

        login_object = Login(self.driver)
        assert login_object.is_login_form_displayed()

        login_object.enter_username(self.INVALID_USERNAME)
        login_object.enter_password(self.VALID_PASSWORD)
        login_object.click_login()
        # Assert unsuccessful login
        assert self.INVALID_CREDS_ALERT in login_object.invalid_credentials_message()
        time.sleep(3)

    def test_invalid_password(self, setup):
        """
        Test login with an invalid password.
        """
        self.driver = setup
        self.driver.get(self.url)

        login_object = Login(self.driver)
        assert login_object.is_login_form_displayed()

        login_object.enter_username(self.VALID_USERNAME)
        login_object.enter_password(self.INVALID_PASSWORD)
        login_object.click_login()
        # Assert unsuccessful login
        assert self.INVALID_CREDS_ALERT in login_object.invalid_credentials_message()
        time.sleep(3)

    def test_empty_fields(self, setup):
        """
        Test login with empty username and password fields.
        """
        self.driver = setup
        self.driver.get(self.url)

        login_object = Login(self.driver)
        assert login_object.is_login_form_displayed()

        login_object.enter_username("")
        login_object.enter_password("")
        login_object.click_login()

        # Assert error messages for required fields
        assert login_object.required_field_message() in self.REQUIRED_FIELD
        time.sleep(3)

    def test_incorrect_credentials(self, setup):
        """
        Test login with incorrect username and password.
        """
        self.driver = setup
        self.driver.get(self.url)

        login_object = Login(self.driver)
        assert login_object.is_login_form_displayed()

        login_object.enter_username(self.INVALID_USERNAME)
        login_object.enter_password(self.INVALID_PASSWORD)
        login_object.click_login()
        # Assert unsuccessful login
        assert self.INVALID_CREDS_ALERT in login_object.invalid_credentials_message()
        time.sleep(3)

    def test_password_case_sensitivity(self, setup):
        """
        Test login with correct username and password with incorrect capitalization,
        and assert error message.
        """
        self.driver = setup
        self.driver.get(self.url)

        login_object = Login(self.driver)
        assert login_object.is_login_form_displayed()

        # Enter correct username and password with incorrect capitalization
        login_object.enter_username(self.VALID_USERNAME.upper())
        login_object.enter_password(self.VALID_PASSWORD.upper())
        login_object.click_login()

        # Assert unsuccessful login due to case sensitivity
        assert self.INVALID_CREDS_ALERT in login_object.invalid_credentials_message()
        time.sleep(3)

    def test_whitespace_in_fields(self, setup):
        """
        Test login with username/password containing leading/trailing
        whitespace and assert handling.
        """
        self.driver = setup
        self.driver.get(self.url)

        login_object = Login(self.driver)
        assert login_object.is_login_form_displayed()

        # Enter username/password with leading/trailing whitespace
        username_with_whitespace = " " + self.VALID_USERNAME + " "
        password_with_whitespace = self.VALID_PASSWORD

        login_object.enter_username(username_with_whitespace)
        login_object.enter_password(password_with_whitespace)
        login_object.click_login()

        # Add assertions related to handling of whitespace in username/password
        assert self.INVALID_CREDS_ALERT in login_object.invalid_credentials_message()
        time.sleep(3)
