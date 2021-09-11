from selenium.webdriver.common.by import By
from Utilities.baseclass import BaseClass


class LoginPage(BaseClass):

    USERNAME = (By.NAME, "userName")
    PASSWORD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.NAME, "submit")
    SIGNON_LINK = (By.LINK_TEXT, "SIGN-ON")
    REGISTER_LINK = (By.LINK_TEXT, "REGISTER")
    SUPPORT_LINK = (By.LINK_TEXT, "SUPPORT")
    CONTACT_LINK = (By.LINK_TEXT, "CONTACT")

    """Use to get page title"""
    def get_login_page_title(self, title):
        return self.get_title(title)

    """Use to check sign up link"""
    def is_signon_link_exist(self):
        return self.is_visible(self.SIGNON_LINK)

    def is_register_link_exist(self):
        return self.is_visible(self.REGISTER_LINK)

    def is_support_link_exist(self):
        return self.is_visible(self.SUPPORT_LINK)

    def is_contact_link_exist(self):
        return self.is_visible(self.CONTACT_LINK)

    """Use to login to app"""
    def login(self, username, password):
        self.send_keys(self.USERNAME, username)
        self.send_keys(self.PASSWORD, password)
        self.click(self.SUBMIT_BUTTON)