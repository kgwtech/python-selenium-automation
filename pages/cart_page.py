from selenium.webdriver.common.by import By
from pages.main_page import Page


class CartPage(Page):

    """ Main Page Element Locators """
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    # Methods for the cart page

    def verify_empty_cart_msg(self):
        self.verify_text("Your cart is empty", *self.CART_EMPTY_MSG)