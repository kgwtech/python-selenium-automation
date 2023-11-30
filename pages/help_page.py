from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class HelpPage(Page):
    """ Help Page Element Locators """

    SEARCH_FIELD = (By.CSS_SELECTOR, ".search-input")
    SEARCH_BTN = (By.CSS_SELECTOR, "input[title='search help']")
    HELP_HEADER_TEXT = (By.CSS_SELECTOR, "h2[class='custom-h2']")
    MAIN_PAGE_BOXES = (By.CSS_SELECTOR, ".box-column [class='grid_6']")
    MAIN_PAGE_GRID = (By.CSS_SELECTOR, "div.grid_6[style*='padding']")
    RESOURCE_BOXES = (By.CSS_SELECTOR, ".grid_4")
    BROWSE_PAGES_TEXT = (By.XPATH, "//h2[text()='Browse all Help pages']")
    HEADER_RETURNS = (By.XPATH, "//h1[text()=' Returns']")
    HEADER_PROMOTIONS = (By.XPATH, "//h1[text()=' Current promotions']")
    HEADER_TECHNICAL = (By.XPATH, "//h1[text()=' Mobile & app support']")
    TOPIC_SELECTION = (By.CSS_SELECTOR, "[id*='ViewHelpTopics']")

    # Base methods to be utilized in Help Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def open_help_page(self):
        self.open_url("https://help.target.com/help")

    def open_help_return_page(self):
        self.open_url("https://help.target.com/help/SubCategoryArticle?childcat=Returns&parentcat=Returns+%26+Exchanges")

    def search(self, help_search):
        self.input_text(help_search, *self.SEARCH_FIELD)

    def click_search_btn(self):
        self.click(*self.SEARCH_BTN)

    def select_topic(self, topic):
        topic_selection = self.find_element(*self.TOPIC_SELECTION)
        select = Select(topic_selection)
        select.select_by_value(topic)

    # Verification methods to be utilized in Main Page Steps
    """ Verifications """  # //////////////////////////////////////////////////////////////////////////////////////////

    def verify_help_header_text(self):
        self.verify_partial_text('Target Help', *self.HELP_HEADER_TEXT)

    def verify_option_boxes(self, number_1, number_2):
        number_1 = int(number_1)
        number_2 = int(number_2)
        boxes = self.find_elements(*self.MAIN_PAGE_BOXES)
        grid = self.find_elements(*self.MAIN_PAGE_GRID)
        assert len(boxes) == number_1 and len(grid) == number_2, \
            f"Options box has {len(boxes)} and {len(grid)} grid box(es)"

    def verify_resource_boxes(self, number):
        number = int(number)
        re_boxes = self.find_elements(*self.RESOURCE_BOXES)
        assert len(re_boxes) == number, f"Additional resources box has {len(re_boxes)} boxes"

    def verify_browse_pages_text(self):
        self.verify_text("Browse all Help pages", *self.BROWSE_PAGES_TEXT)

    def verify_return_page_opened(self):
        self.wait_for_visibility(*self.HEADER_RETURNS)

    def verify_promotions_opened(self):
        self.wait_for_visibility(*self.HEADER_PROMOTIONS)

    def verify_tech_supp_page_opened(self):
        self.wait_for_visibility(*self.HEADER_TECHNICAL)

