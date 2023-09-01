"""
Defines the Login class for handling login-related web page actions.
"""

# Third-party
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Login:
    """
    Class for handling login related web-page actions.
    """

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    login_form = "//div[@class='orangehrm-login-form']"
    forgot_password_link_v1 = ".//*[text()='Forgot your password?']"
    forgot_password_link_v2 = "//p[text() ='Forgot your password? ']"
    forgot_password_header = "//p[contains(@class, 'orangehrm-login-forgot-header')]"
    username_field = "//input[@name='username']"
    password_field = "//input[@name='password']"
    reset_password_button = (
        "//button[contains(@class, 'orangehrm-forgot-password-button--reset')]"
    )
    reset_link_sent_message = "//*[text()='Reset Password link sent successfully']"
    user_drop_down_menu = "//li[@class='oxd-userdropdown']"
    drop_down_menu = "//ul[@class='oxd-dropdown-menu']"
    login_button = "//button[@type='submit']"
    logout_button = "//li/a[contains(@href,'logout')]"
    login_form_error = "//div[@class='orangehrm-login-error']"
    required_field = "//span[contains(@class, 'oxd-input-field-error-message')]"

    def __init__(self, driver):
        """
        Initialize the Admin instance.
        :param driver: WebDriver instance for controlling the browser.
        """
        self.driver = driver
        self.driver.maximize_window()

    def click_url(self):
        """
        Open the specified URL.
        """
        self.driver.get(self.url)

    def enter_username(self, username):
        """
        Enter the username and press Enter.
        :param username: str: Username to be entered.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.username_field))
        )
        element.send_keys(username)

    def enter_password(self, password):
        """
        Enter the password.
        :param password: str: Password to be entered.
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.password_field))
        ).send_keys(password)

    def click_login(self):
        """
        Click the login button.
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.login_button))
        ).click()

    def click_forgot_password_link(self):
        """
        Click the 'Forgot your password?' link.
        """
        try:
            header_elem = WebDriverWait(self.driver, 10).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, self.forgot_password_header)
                )
            )
            WebDriverWait(header_elem, 10).until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, self.forgot_password_link_v1)
                )
            ).click()
        except:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, self.forgot_password_link_v2)
                )
            ).click()

    def click_reset_password_button(self):
        """
        Click the 'Reset Password' button.
        """
        button = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.reset_password_button)
            )
        )
        button.click()

    def check_reset_link_sent_message(self):
        """
        Check if the 'Reset Password link sent successfully' message is displayed.
        """
        element = WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.reset_link_sent_message)
            )
        )
        return element.is_displayed()

    def view_drop_down_menu(self):
        """
        View the user drop-down menu.
        """
        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.user_drop_down_menu)
            )
        ).click()

        WebDriverWait(self.driver, 30).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.drop_down_menu)
            )
        )

    def click_logout(self):
        """
        Click the logout button.
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.logout_button))
        ).click()

    def is_login_form_displayed(self):
        """
        Check if the login form is displayed.
        """
        login_form = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located((By.XPATH, self.login_form))
        )
        return login_form.is_displayed()

    def invalid_credentials_message(self):
        """
        Get the invalid credentials error message.
        """
        alert_message = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.login_form_error)
            )
        )
        return alert_message.text

    def required_field_message(self):
        """
        Get the required field error message.
        """
        alert_message = WebDriverWait(self.driver, 10).until(
            expected_conditions.presence_of_element_located(
                (By.XPATH, self.login_form_error)
            )
        )
        required_field_message = alert_message.find_element(
            By.XPATH, self.required_field
        )
        return required_field_message.text
