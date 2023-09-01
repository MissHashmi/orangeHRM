"""
Module Description: Test cases for the Admin Page.

This module contains test cases to validate the functionality of the Admin Page.
"""

# Standard library
import time

# Third-party
import pytest
from selenium import webdriver

# First-party
from pageObjects.adminPage import AdminHeader, AdminMainMenu
from pageObjects.loginPage import Login


@pytest.fixture()
def setup():
    """
    Fixture to set up the WebDriver instance before running each test case.
    """
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestAdminPage:
    """
    Test class for validating the Admin Page.
    """

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    ADMIN_USERNAME = "Admin"
    ADMIN_PASSWORD = "admin123"

    def test_validate_header_options(self, setup):
        """
        Test if the header options on the admin page are displayed correctly.
        """
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(2)

        login_object = Login(self.driver)
        login_object.enter_username(self.ADMIN_USERNAME)
        login_object.enter_password(self.ADMIN_PASSWORD)
        login_object.click_login()

        admin_object = AdminHeader(self.driver)
        admin_object.click_admin_tab()

        assert admin_object.is_job_displayed()
        assert admin_object.is_organization_displayed()
        assert admin_object.is_qualifications_displayed()
        assert admin_object.is_nationalities_displayed()
        assert admin_object.is_corporate_branding_displayed()
        assert admin_object.is_configuration_displayed()

    def test_validate_main_menu_options(self, setup):
        """
        Test if the main menu options on the admin side panel are displayed correctly.
        """
        self.driver = setup
        self.driver.get(self.url)
        time.sleep(2)

        login_object = Login(self.driver)
        login_object.enter_username(self.ADMIN_USERNAME)
        login_object.enter_password(self.ADMIN_PASSWORD)
        login_object.click_login()

        admin_object = AdminMainMenu(self.driver)
        admin_object.click_admin_tab()

        assert admin_object.is_admin_displayed()
        assert admin_object.is_pim_displayed()
        assert admin_object.is_leave_displayed()
        assert admin_object.is_time_displayed()
        assert admin_object.is_recruitment_displayed()
        assert admin_object.is_my_info_displayed()
        assert admin_object.is_performance_displayed()
        assert admin_object.is_dashboard_displayed()
        assert admin_object.is_directory_displayed()
        assert admin_object.is_maintenance_displayed()
        assert admin_object.is_claim_displayed()
        assert admin_object.is_buzz_displayed()
