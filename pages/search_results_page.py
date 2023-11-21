from selenium.webdriver.common.by import By
from pages.base_page import Page
from time import sleep


class SearchResultsPage(Page):

    """ Search Results Page Element Locators """
    SEARCH_RESULTS_TXT = (By.CSS_SELECTOR, "[data-test='resultsHeading']")
    LISTINGS = (By.CSS_SELECTOR, "[data-test='@web/site-top-of-funnel/ProductCardWrapper']")
    PRODUCT_TITLE = (By.CSS_SELECTOR, "[data-test='product-title']")
    PRODUCT_IMG = (By.CSS_SELECTOR, "[class*='ProductCardImage']")

    # Methods for the Search Results Page
    def verify_search_result(self, expected_product):
        search_results_header = self.find_element(*self.SEARCH_RESULTS_TXT).text
        assert expected_product in search_results_header, \
            f'Expected text {expected_product} not in {search_results_header}'

    def verify_search_url(self, expected_url):
        assert expected_url in self.driver.current_url, \
            f"Expected {expected_url} not in {self.driver.current_url}"

    def verify_products_name_img(self):
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        sleep(2)  # wait for loading/ads
        self.driver.execute_script("window.scrollBy(0,2000)", "")
        all_products = self.driver.find_elements(*self.LISTINGS)
        # print(len(all_products)) # for verification for number of products

        for product in all_products:
            # print(product.text) #
            title = product.find_element(*self.PRODUCT_TITLE).text
            print(title)
            assert title, 'Product title not shown'
            product.find_element(*self.PRODUCT_IMG)

