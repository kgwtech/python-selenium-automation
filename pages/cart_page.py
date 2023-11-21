from selenium.webdriver.common.by import By
from pages.main_page import Page


class CartPage(Page):

    """ Main Page Element Locators """
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    CART_EMPTY_MSG = (By.CSS_SELECTOR, "[data-test='boxEmptyMsg']")

    # Methods for the cart page

    def click_icon_from_main(self):
        self.click(*self.CART_ICON)

    def verify_empty_cart_msg(self):
        self.find_element(*self.CART_EMPTY_MSG)
