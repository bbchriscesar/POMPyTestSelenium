import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Utilities.config import TestData


@pytest.fixture(params=["chrome"], scope='class')
def setup(request):
    global web_driver
    if request.param == "chrome":
        web_driver = webdriver.Chrome(ChromeDriverManager().install())
        web_driver.delete_all_cookies()
        web_driver.maximize_window()
    if request.param == "firefox":
        web_driver = webdriver.Firefox(executable_path=GeckoDriverManager().install())
        web_driver.delete_all_cookies()
        web_driver.maximize_window()
    web_driver.get(TestData.BASE_URL)
    request.cls.driver = web_driver
    yield
    web_driver.quit()