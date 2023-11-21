from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SignInPage(Page):

    """ SignIn Page Element Locators """

    USERNAME_FIELD = (By.CSS_SELECTOR, "#username")
    PASSWORD_FIELD = (By.CSS_SELECTOR, "#password")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "#login")
    SIGN_IN_TXT = (By.CSS_SELECTOR, "h1[class*=AuthHeading]")

    # Base methods to be utilized in SignIn Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def signin(self, username, password):
        self.input_text(text=username, *self.USERNAME_FIELD)
        self.input_text(text=password, *self.PASSWORD_FIELD)
        self.click(*self.SIGN_IN_BTN)

    # Verification methods to be utilized in SignIn Page Steps
    """ Verifications """  # //////////////////////////////////////////////////////////////////////////////////////////

    def verify_page_opened(self):
        self.verify_text("Sign into your Target account", *self.SIGN_IN_TXT)
