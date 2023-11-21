from selenium.webdriver.common.by import By
from behave import *

""" Calls methods from the Page Object for Webpage under test """

ADD_TO_CART_BTN = (By.CSS_SELECTOR, "[data-test='addToCartButton']")
SIDE_NAV_PRODUCT_NAME = (By.CSS_SELECTOR, "h4[class*='StyledHeading']")


# @when('Click on Add to Cart button')
# def store_product_name(context):


@given('Open target product page')
def open_page(context):
    context.driver.get('https://www.target.com/p/A-87877683')


@then('Verify search worked for {product}')
def verify_search_result(context, product):
    context.app.search_results_page.verify_search_result(product)


@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    context.app.search_results_page.verify_search_url(expected_keyword)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    context.app.search_results_page.verify_products_name_img()
