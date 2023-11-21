from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):

    """ Search Results Page Element Locators """

    SEARCH_RESULTS_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")
    LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")
    ADD_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
    SIDE_MENU_ITEM_ADDED_TXT = (By.CSS_SELECTOR, "h2[class*='StyledHeading'] [class='h-text-lg']")

    # Base methods to be utilized in Search Results Page Steps
    """ Base Methods"""  # ////////////////////////////////////////////////////////////////////////////////////////////

    def add_product_to_cart(self):
        self.driver.execute_script("window.scrollBy(0,1000)", "")
        self.find_elements(*self.ADD_CART_BTN)[0].click()

    # Verification methods to be utilized in Search Results Page Steps
    """ Verifications """  # //////////////////////////////////////////////////////////////////////////////////////////

    def verify_product_in_cart(self):
        self.wait_for_visibility(*self.SIDE_MENU_ITEM_ADDED_TXT)
        self.verify_text("Added to cart", *self.SIDE_MENU_ITEM_ADDED_TXT)

    def verify_search_result(self, expected_product):
        self.verify_partial_text(expected_product, *self.SEARCH_RESULTS_TXT)

    def verify_search_url(self, expected_url):
        self.verify_partial_url(expected_url)

    def verify_products_name_img(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        # sleep(2)  # wait for loading/ads
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        all_products = self.driver.find_elements(*self.LISTINGS)
        # print(len(all_products)) # for verification for number of products

        for product in all_products:
            # print(product.text) #
            title = product.find_element(*self.PRODUCT_TITLE).text
            print(title)
            assert title, 'Product title not shown'
            product.find_element(*self.PRODUCT_IMG)

