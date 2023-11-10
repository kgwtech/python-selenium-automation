from selenium.webdriver.common.by import By
from behave import *
from time import sleep


@then('Navigate to Circle page')
def navigate_circle(context):
    context.driver.find_element(By.CSS_SELECTOR, "#utilityNav-circle").click()
    sleep(3)  # allow for circle page to load


@then('Verify circle page is displayed')
def navigate_circle(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "[data-test='circle-logo']").is_displayed(), \
        f"Circle logo not found"


@then('Verify {number} benefit boxes are displayed')
def navigate_circle(context, number):
    number = int(number)
    benefits = context.driver.find_elements(By.CSS_SELECTOR, "[class*='BenefitCard-sc']")
    assert len(benefits) == number, f"Expected 5 benefit boxes, {len(benefits)} boxes were displayed."
