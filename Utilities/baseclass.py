import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.mark.usefixtures("setup")
class BaseClass:

    def click(self, by_locator):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).click()
        #print(f"Click the element {by_locator} locator")

    def send_keys(self, by_locator, text):
        WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
        #print(f"Send text {text} to the locator {by_locator}")

    def get_element_text(self, by_locator):
        element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(by_locator))
        #print('Get the element text ' + element.text + ' from the locator ' + by_locator)
        return element.text

    def is_visible(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        #print(f"Checking if element {by_locator} is visible")
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 30).until(EC.title_is(title))
        #print(f"Get the page title {title}")
        return self.driver.title