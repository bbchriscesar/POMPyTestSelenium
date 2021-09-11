from selenium.webdriver.common.by import By
from Utilities.baseclass import BaseClass


class HomePage(BaseClass):

    LOGIN_SUCCESSFUL_TEXT = (By.XPATH, "//h3[text()='Login Successfully']")
    THANKYOU_LOGIN_TEXT = (By.XPATH, "//b[text()=' Thank you for Loggin. ']")

    def get_home_page_title(self, title):

        return self.get_title(title)

    def get_successful_homepage_login_text(self):
        return self.get_element_text(self.LOGIN_SUCCESSFUL_TEXT)

    def get_thank_you_login_text(self):
        return self.get_element_text(self.THANKYOU_LOGIN_TEXT)