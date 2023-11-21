from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class CirclePage(Page):

    """ Main Page Element Locators """

    TABS = (By.CSS_SELECTOR, "[class*='PageSelectionText'] a")
    CIRCLE_HEADER_LOGO = (By.CSS_SELECTOR, "[data-test='circle-logo']")

    # Base methods to be utilized in Circle Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////
    def open_circle_page(self):
        self.open_url("https://www.target.com/circle")
        sleep(5)  # wait for ads

    # Verification methods to be utilized in Circle Page Steps
    """ Verifications """  # //////////////////////////////////////////////////////////////////////////////////////////

    def verify_tabs_clickable(self):
        tabs = self.find_elements(*self.TABS)
        # StaleElementReferenceException Solution:
        current_url = ''
        for i in range(len(tabs)):  # (0, 1, 2, 3)
            self.find_elements(*self.TABS)[i].click()
            self.wait_for_url_change(current_url)
            current_url = self.driver.current_url

    def verify_num_tabs_displayed(self, number):
        number = int(number)
        tabs = self.driver.find_elements(*self.TABS)
        assert len(tabs) == number, f"Expected 4 tabs, {len(tabs)} tabs were displayed"