
from selenium.webdriver.common.by import By

from app_for_web.pages.base_page import BasePage


class SuccessfulSignupPopup(BasePage):

    _MODAL_LOCATOR = "//div[contains(@class, 'popup_is-opened')]"
    _CLOSE_BUTTON_LOCATOR = By.XPATH, f"{_MODAL_LOCATOR}//button"
    _LABEL_LOCATOR = By.XPATH, f"{_MODAL_LOCATOR}//p"

    SIGNUP_TEXT = "Вы успешно зарегистрировались"

    def __init__(self, driver):
        super().__init__(driver)

    def get_text(self):
        return self.find_element(self._LABEL_LOCATOR).text

    def click_close_button(self):
        self.click_element(self._CLOSE_BUTTON_LOCATOR)
