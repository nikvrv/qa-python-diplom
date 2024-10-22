import allure

from app_for_web.pages.signup_page import SignUpPage
from app_for_web.pages.successful_popup import SuccessfulSignupPopup
from data import WEB_APP_URL
from helpers import get_sign_up_data


class TestSignUp:

    @allure.title("Signup")
    def test_signup_pom(self, driver):
        email_data, password_data = get_sign_up_data()
        sign_up_page = SignUpPage(driver)
        sign_up_page.open_page(WEB_APP_URL)
        sign_up_page.enter_email(email_data)
        sign_up_page.enter_password(password_data)
        sign_up_page.submit_button_click()

        modal = SuccessfulSignupPopup(driver)

        assert modal.get_text() == modal.SIGNUP_TEXT
