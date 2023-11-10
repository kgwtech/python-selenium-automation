from selenium.webdriver.common.by import By
from behave import *
from time import sleep


@given('Open target help page')
def open_help_page(context):
    context.driver.get("https://help.target.com/help")


@then("Verify 'Target Help' text")
def click_help_button(context):
    expected_text = context.driver.find_element(By.CSS_SELECTOR, "h2[class='custom-h2']").text
    assert 'Target Help' in expected_text, f"'Target Help' not in {expected_text}]"


@then('Enter {help_search} in text field')
def enter_text(context, help_search):
    context.driver.find_element(By.CSS_SELECTOR, ".search-input").send_keys(help_search)
    sleep(3)  # Can see search field has text entered


@then('Click search icon button')
def verify_search_icon(context):
    context.driver.find_element(By.CSS_SELECTOR, "input[title='search help']").click()


@then('Verify options box has {number_1} boxes and {number_2} grid box')
def verify_option_boxes(context, number_1, number_2):
    # Code-block is a bit much, but this is the only I could produce a result
    number_1 = int(number_1)
    number_2 = int(number_2)
    boxes = context.driver.find_elements(By.CSS_SELECTOR, ".box-column [class='grid_6']")
    grid = context.driver.find_elements(By.CSS_SELECTOR, "div.grid_6[style*='padding']")
    assert len(boxes) == number_1 and len(grid) == number_2, \
        f"Options box has {len(boxes)} and {len(grid)} grid box(es) "


@then('Verify additional resources box has {number} boxes')
def verify_resource_boxes(context, number):
    number = int(number)
    re_boxes = context.driver.find_elements(By.CSS_SELECTOR, ".grid_4")
    assert len(re_boxes) == number, f"Additional resources box has {len(re_boxes)} boxes"


@then("Verify 'Browse all Help pages' text")
def click_browse(context):
    expected_text = context.driver.find_element(By.XPATH, "//h2[text()='Browse all Help pages']").text
    assert "Browse all Help pages" in expected_text, f"Actual text is {expected_text}"
