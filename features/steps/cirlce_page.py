from selenium.webdriver.common.by import By
from behave import *

""" Calls methods from the Page Object for Webpage under test """


@given('Open target Circle Page')
def open_circle(context):
    context.app.circle_page.open_circle_page()


@then('Verify circle page is displayed')
def navigate_circle(context):
    assert context.driver.find_element(By.CSS_SELECTOR, "[data-test='circle-logo']").is_displayed(), \
        f"Circle logo not found"


@then('Verify {number} tabs are displayed')
def verify_num_tabs(context, number):
    context.app.circle_page.verify_num_tabs_displayed(number)


@then('Verify user can click through tabs')
def verify_tabs_clickable(context):
    context.app.circle_page.verify_tabs_clickable()