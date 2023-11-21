from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):

    """ Main Page Element Locators """
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIDE_MENU_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
    HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")


    # Methods for the Main Page
    def open_main(self):
        self.open_url("https://www.target.com/")

    def search(self, product):
        self.input(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)  # wait for ads to disappear

    def click_signin(self):
        self.click(*self.SIGN_IN_BTN)

    def signin_from_nav(self):
        self.click(*self.SIDE_MENU_SIGN_IN)

    def verify_header(self):
        self.find_element(*self.HEADER)

    def verify_header_links(self, number):
        number = int(number)  # convert str to int
        links = self.find_element(*self.HEADER_LINKS)
        assert len(links) == number, f"Expected {number} links, but received {len(links)}"

    def click_cart_icon(self):
        self.click(*self.CART_ICON)


