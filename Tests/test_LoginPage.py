import pytest
from Pages.LoginPage import LoginPage
from Utilities.config import TestData


@pytest.mark.login
class LoginTests(LoginPage):

    def test_LoginPage(self):
        
        """Checking page title"""
        title = self.get_login_page_title(TestData.WELCOME_PAGE_TITLE)
        assert title == TestData.WELCOME_PAGE_TITLE

        """Checking links"""
        assert self.is_signon_link_exist()
        assert self.is_register_link_exist()
        assert self.is_support_link_exist()
        assert self.is_contact_link_exist()

        """Login to webapp"""
        self.login(TestData.USER_NAME, TestData.PASSWORD)