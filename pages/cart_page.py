from selenium.webdriver.common.by import By
from pages.main_page import Page


class CartPage(Page):

    """ Cart Page Element Locators """

    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    # Base methods to be utilized in Cart Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    # Verification methods to be utilized in Cart Page Steps
    """ Verifications """  # //////////////////////////////////////////////////////////////////////////////////////////

    def verify_empty_cart_msg(self):
        self.verify_text("Your cart is empty", *self.CART_EMPTY_MSG)