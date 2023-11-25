from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class PartnerPage(Page):

    """ Partner Page Element Locators """
    TERMS_CONDITIONS_HEADER = (By.CSS_SELECTOR, "[data-test='page-title']")

    # Base methods to be utilized in Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def verify_google_play_opened(self):
        self.verify_partial_url('https://play.google.com/')

    def verify_terms_conditions_opened(self):
        self.verify_text("Terms & Conditions", *self.TERMS_CONDITIONS_HEADER)