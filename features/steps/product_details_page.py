from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from time import sleep

COLORS = (By.CSS_SELECTOR, "[class*='ButtonWrapper'] img")
CURRENT_COLOR = (By.CSS_SELECTOR, "div[class*='VariationSelectorImage'] div[class*='CellVariationHeaderWrapper']")
PRODUCTS = (By.CSS_SELECTOR, "div[class*='StyledRow'] div[class*='dOpyUp']")
PRODUCT_TITLES = (By.CSS_SELECTOR, "a[data-test='product-title']")


@given('Open target product page')
def open_page(context):
    context.driver.get('https://www.target.com/p/A-87877683')


@then('Click and verify colors and names of product correspond')
def click_product(context):
    colors = context.driver.find_elements(*COLORS)
    expected_names = ["Blue", "Pink", "Silver", "Yellow"]
    actual_names = []
    sleep(5)  # wait for ads, could not find EC method
    for color in colors:
        color.click()
        current_color = context.driver.find_element(*CURRENT_COLOR).text.split("\n")[1]
        actual_names.append(current_color)
    assert expected_names == actual_names, f"{expected_names} not in {actual_names}"


@then("Search for {product}")
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(5) # wait for ads to disappear


@then("Verify all products display a name")
def verify_names(context):
 # struggled with creating verification

    # products = context.driver.find_elements(*PRODUCTS)
    # for product in products:
    #     assert product.is_displayed()
    #     context.driver.wait.until(EC.presence_of_all_elements_located(PRODUCT_TITLES))
    #     current_title = context.driver.find_element(*PRODUCT_TITLES).text
    #     assert current_title.is_displayed()


@then("Verify all products display an image")
def verify_images(context):
# # struggled with creating verification