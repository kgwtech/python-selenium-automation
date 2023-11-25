from pages.base_page import Page
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.main_page import MainPage
from pages.partner_page import PartnerPage
from pages.search_results_page import SearchResultsPage
from pages.signin_page import SignInPage


class Application:
    # Establishes links between Page Objects and Behave context
    # Give access to driver
    # Gives usability of methods from pages
    def __init__(self, driver):
        # Base
        self.page = Page(driver)

        # Page Objects
        self.cart_page = CartPage(driver)
        self.circle_page = CirclePage(driver)
        self.main_page = MainPage(driver)
        self.partner_page = PartnerPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.signin_page = SignInPage(driver)


