from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import Page
from time import sleep


class SignInPage(Page):

    """ SignIn Page Element Locators """

    # SignIn email: "telme0@btcmod.com"
    # SignIn pass: "newfakepass123"

    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    SIGN_IN_BTN = (By.ID, "login")
    SIGN_IN_TXT = (By.CSS_SELECTOR, "h1[class*=AuthHeading]")
    SIGNED_IN_MSG = (By.CSS_SELECTOR, "[class*='LinkText']")
    TERMS_CONDITIONS = (By.CSS_SELECTOR, "[aria-label*='terms']")

    # Base methods to be utilized in SignIn Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////
    def open_signin_page(self):
        self.open_url("https://www.target.com/login?client_id=ecom-web-1.0.0&ui_namespace=ui-default"
                      "&back_button_action=browser&keep_me_signed_in=true&kmsi_default=false&actions"
                      "=create_session_signin")

    def input_credentials(self, username, password):
        self.wait_for_visibility(*self.USERNAME_FIELD)
        self.input_text(username, *self.USERNAME_FIELD)
        self.wait_for_visibility(*self.PASSWORD_FIELD)
        self.input_text(password, *self.PASSWORD_FIELD)

    def login(self):
        self.wait_for_visibility(*self.SIGN_IN_BTN)
        self.click(*self.SIGN_IN_BTN)
        sleep(2)

    def click_terms_conditions(self):
        self.wait.until(EC.presence_of_element_located(self.TERMS_CONDITIONS))
        self.click(*self.TERMS_CONDITIONS)

    # Verification methods to be utilized in SignIn Page Steps
    """ Verifications """  # //////////////////////////////////////////////////////////////////////////////////////////

    def verify_page_opened(self):
        self.verify_text("Sign into your Target account", *self.SIGN_IN_TXT)


    def verify_login(self):
        self.verify_text("Hi, ", *self.SIGNED_IN_MSG)