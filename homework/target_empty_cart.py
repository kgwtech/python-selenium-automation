from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click on cart icon')
def click_cart(context):
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/CartLink']").click()
    sleep(5)


@then('Verify cart is empty message shown')
def verify_message(context):
    empty_message = context.driver.find_element(By.XPATH, "//h1[text()='Your cart is empty']").text
    assert "Your cart is empty" in empty_message, f"Expected text not in {empty_message}"
