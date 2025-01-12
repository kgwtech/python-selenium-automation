from selenium.webdriver.common.by import By
from behave import *

""" Calls methods from the Page Object for Webpage under test """


# @when('Click on Add to Cart button')
# def store_product_name(context):


@given('Open target product page')
def open_page(context):
    context.driver.get('https://www.target.com/p/A-87877683')


@then('Add item to cart')
def add_product_to_cart(context):
    context.app.search_results_page.add_product_to_cart()


@then('Verify product is in cart')
def verify_product_in_cart(context):
    context.app.search_results_page.verify_product_in_cart()


@then('Verify search worked for {product}')
def verify_search_result(context, product):
    context.app.search_results_page.verify_search_result(product)


@then('Verify {expected_keyword} in search result url')
def verify_search_url(context, expected_keyword):
    context.app.search_results_page.verify_search_url(expected_keyword)


@then('Verify that every product has a name and an image')
def verify_products_name_img(context):
    context.app.search_results_page.verify_products_name_img()
