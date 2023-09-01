"""
Module for interacting with the admin page on a web page.
"""

# Third-party
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Admin:
    """
    Base class for interacting with the admin page on a web page.
    """

    url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
    admin_tab = "//a[@href='/web/index.php/admin/viewAdminModule']"
    user_name = "//input[@name='username']"
    password = "//input[@name='password']"
    submit = "//button[@type='submit']"

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

    def click_admin_tab(self):
        """
        Click the Admin tab.
        """
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.admin_tab))
        ).click()


class AdminHeader(Admin):
    """
    Class for interacting with the admin header options on a web page.
    """

    invalid_creds_msg = "//p[text()='Invalid credentials']"
    creds_req = "//span[text()='Required']"
    admin_tab = "//a[@href='/web/index.php/admin/viewAdminModule']"
    user_management = "//span[contains(text(), 'User Management')]"
    organization = "//span[contains(text(), 'Organization')]"
    qualifications = "//span[contains(text(), 'Qualifications')]"
    nationalities = "//a[contains(text(), 'Nationalities')]"
    corporate_branding = "//a[contains(text(), 'Corporate Branding')]"
    configuration = "//span[contains(text(), 'Configuration')]"
    job = "//span[contains(text(), 'Job')]"

    def is_job_displayed(self):
        """
        Check if the Job header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.job))
        )
        return element.is_displayed()

    def is_organization_displayed(self):
        """
        Check if the Organization header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.organization))
        )
        return element.is_displayed()

    def is_user_management_displayed(self):
        """
        Check if the User Management header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.user_management)
            )
        )
        return element.is_displayed()

    def is_qualifications_displayed(self):
        """
        Check if the Qualifications header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.qualifications))
        )
        return element.is_displayed()

    def is_nationalities_displayed(self):
        """
        Check if the Nationalities header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.nationalities))
        )
        return element.is_displayed()

    def is_corporate_branding_displayed(self):
        """
        Check if the Corporate Branding header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(
                (By.XPATH, self.corporate_branding)
            )
        )
        return element.is_displayed()

    def is_configuration_displayed(self):
        """
        Check if the Configuration header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.configuration))
        )
        return element.is_displayed()


class AdminMainMenu(Admin):
    """
    Class for interacting with the admin main menu on a web page.
    """

    admin_tab = "//a[@href='/web/index.php/admin/viewAdminModule']"
    admin = "//a[contains(@href,'Admin')]"
    pim = "//a[contains(@href,'Pim')]"
    leave = "//a[contains(@href,'Leave')]"
    time = "//a[contains(@href,'Time')]"
    recruitment = "//a[contains(@href,'viewRecruitmentModule')]"
    my_info = "//a[contains(@href,'MyDetails')]"
    performance = "//a[contains(@href,'viewPerformanceModule')]"
    dashboard = "//a[contains(@href,'/dashboard')]"
    directory = "//a[contains(@href,'viewDirectory')]"
    maintenance = "//a[contains(@href,'viewMaintenanceModule')]"
    claim = "//a[contains(@href,'viewClaimModule')]"
    buzz = "//a[contains(@href,'viewBuzz')]"

    def is_pim_displayed(self):
        """
        Check if PIM header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.pim))
        )
        return element.is_displayed()

    def is_leave_displayed(self):
        """
        Check if Leave header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.leave))
        )
        return element.is_displayed()

    def is_time_displayed(self):
        """
        Check if Time header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.time))
        )
        return element.is_displayed()

    def is_recruitment_displayed(self):
        """
        Check if Recruitment header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.recruitment))
        )
        return element.is_displayed()

    def is_my_info_displayed(self):
        """
        Check if My Info header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.my_info))
        )
        return element.is_displayed()

    def is_performance_displayed(self):
        """
        Check if Performance header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.performance))
        )
        return element.is_displayed()

    def is_dashboard_displayed(self):
        """
        Check if Dashboard header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.dashboard))
        )
        return element.is_displayed()

    def is_directory_displayed(self):
        """
        Check if Directory header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.directory))
        )
        return element.is_displayed()

    def is_maintenance_displayed(self):
        """
        Check if Maintenance header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.maintenance))
        )
        return element.is_displayed()

    def is_admin_displayed(self):
        """
        Check if Admin header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.admin_tab))
        )
        return element.is_displayed()

    def is_claim_displayed(self):
        """
        Check if Claim header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.claim))
        )
        return element.is_displayed()

    def is_buzz_displayed(self):
        """
        Check if Buzz header is displayed.
        """
        element = WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable((By.XPATH, self.buzz))
        )
        return element.is_displayed()
