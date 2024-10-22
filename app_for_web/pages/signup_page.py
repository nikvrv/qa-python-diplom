
from selenium.webdriver.common.by import By

from app_for_web.pages.base_page import BasePage


class SignUpPage(BasePage):

    _EMAIL_FIELD = By.XPATH, "//*[@id='email']"
    _PASSWORD_FIELD = By.XPATH, "//*[@id='password']"
    _SUBMIT_BUTTON = By.XPATH, "//button[contains(@class, 'auth')]"

    def __init__(self, driver):
        super().__init__(driver)

    def open_page(self, url):
        self.navigate(f"{url}/signup")

    def enter_email(self, email):
        self.enter_text(self._EMAIL_FIELD, email)

    def enter_password(self, password):
        self.enter_text(self._PASSWORD_FIELD, password)

    def submit_button_click(self):
        self.click_element(self._SUBMIT_BUTTON)
