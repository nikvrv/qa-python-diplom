import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def navigate(self, url):
        with allure.step("Open page"):
            self.driver.get(url)

    def find_element(self, locator, timeout=10):
        with allure.step(f"Find element with locator {locator}"):
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located(locator)
            )

    def find_elements(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.presence_of_all_elements_located(locator)
        )

    def click_element(self, locator, timeout=10):
        with allure.step(f"CLick element with locator {locator}"):
            self.find_element(locator, timeout).click()

    def enter_text(self, locator, text, timeout=10):
        with allure.step(f"Fill text {text} into field with locator {locator}"):
            self.find_element(locator, timeout).send_keys(text)

    def wait_for_element_visible(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def element_is_present(self, locator, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True
        except TimeoutException:
            return False
