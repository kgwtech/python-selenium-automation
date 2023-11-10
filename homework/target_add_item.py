from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Item is added to cart')
def add_items(context):
    search_bar = context.driver.find_element(By.ID, "search")
    search_bar.send_keys('body wash')
    context.driver.find_element(By.XPATH, "//button[@aria-label='search']").click()
    sleep(5)
    item_1 = context.driver.find_element(By.ID, "addToCartButtonOrTextIdFor16249119")
    item_1.click()


@then('Verify item is in cart')
def verify_items(context):
    verify_text = context.driver.find_element(By.XPATH, "//span[text()='Added to cart']").text
    assert "Added to cart" in verify_text, f"Text not in {verify_text}"