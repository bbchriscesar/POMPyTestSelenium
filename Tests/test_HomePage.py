import pytest
from Pages.HomePage import HomePage
from Pages.LoginPage import LoginPage
from Utilities.config import TestData


@pytest.mark.homepage
class HomePageTests(HomePage, LoginPage):

    def test_LoginPage(self):
        self.login(TestData.USER_NAME, TestData.PASSWORD)

    @pytest.mark.depends(on=['test_LoginPage'])
    def test_HomePage(self):
        title = self.get_home_page_title(TestData.LOGIN_PAGE_TITLE)
        assert title == TestData.LOGIN_PAGE_TITLE

        successLogin = self.get_successful_homepage_login_text()
        assert successLogin == TestData.LOGIN_SUCCESSFUL

        thankYouText = self.get_thank_you_login_text()
        assert thankYouText == TestData.THANK_YOU_LOGIN

