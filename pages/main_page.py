from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class MainPage(Page):

    """ Main Page Element Locators """
    SEARCH_FIELD = (By.ID, 'search')
    SEARCH_BTN = (By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']")
    SIGN_IN_BTN = (By.CSS_SELECTOR, "[data-test='@web/AccountLink']")
    SIGN_IN_ARROW = (By.CSS_SELECTOR, "[data-test='@web/AccountLink'] > div > svg.expander")
    SIDE_MENU_SIGN_IN = (By.CSS_SELECTOR, "[data-test='accountNav-signIn']")
    HEADER = (By.CSS_SELECTOR, "[class*='UtilityHeaderWrapper']")
    HEADER_LINKS = (By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    CART_ICON = (By.CSS_SELECTOR, "[data-test='@web/CartLink']")
    CIRCLE_PAGE_LINK = (By.CSS_SELECTOR, "#utilityNav-circle")

    # Base methods to be utilized in Main Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def open_main(self):
        self.open_url("https://www.target.com/")

    def nav_to_circle_page(self):
        self.click(*self.CIRCLE_PAGE_LINK)

    def search(self, product):
        self.input_text(product, *self.SEARCH_FIELD)
        self.click(*self.SEARCH_BTN)
        sleep(6)  # wait for ads to disappear

    def click_signin(self):
        self.click(*self.SIGN_IN_BTN)

    def click_cart_icon(self):
        self.wait_for_element_click(*self.CART_ICON)

    def signin_from_nav(self):
        self.wait_for_visibility(*self.SIDE_MENU_SIGN_IN)
        self.click(*self.SIDE_MENU_SIGN_IN)

    def hover_over_signin(self):
        signin_btn = self.find_element(*self.SIGN_IN_BTN)
        actions = ActionChains(self.driver)
        actions.move_to_element(signin_btn)
        actions.perform()


    # Verification methods to be utilized in Main Page Steps
    """ Verifications """  # //////////////////////////////////////////////////////////////////////////////////////////

    def verify_header(self):
        self.find_element(*self.HEADER)

    def verify_header_links(self, number):
        number = int(number)  # convert str to int
        links = self.find_element(*self.HEADER_LINKS)
        assert len(links) == number, f"Expected {number} links, but received {len(links)}"

    def verify_signin_arrow_shown(self):
        self.wait_for_visibility(*self.SIGN_IN_ARROW)



