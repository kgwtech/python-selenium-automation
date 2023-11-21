from pages.base_page import Page
from pages.cart_page import CartPage
from pages.circle_page import CirclePage
from pages.main_page import MainPage
from pages.search_results_page import SearchResultsPage


class Application:
    # Establishes links between Page Objects and Behave context
    # Give access to driver
    # Gives usability of methods from pages
    def __init__(self, driver):
        self.page = Page(driver)  # Base

        self.cart_page = CartPage(driver)
        self.main_page = MainPage(driver)
        self.search_results_page = SearchResultsPage(driver)
        self.circle_page = CirclePage(driver)


