from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from behave import *
from time import sleep

""" Calls methods from the Page Object for Webpage under test """


@given('Open target Circle Page')
def open_circle(context):
    context.app.circle_page.open_circle_page()


@given('Store original window')
def store_original_window(context):
    context.windows = context.app.page.get_all_windows()
    context.original_window = context.app.page.get_current_window()
    # print('All windows', context.windows)
    # print('Current window', context.original_window)


@when('Click Google Play button')
def click_play_button(context):
    context.app.circle_page.click_google_play_btn()


@when('Switch to new window')
def switch_window(context):
    context.app.page.switch_to_new_window()


@then('Close current page')
def close_current_page(context):
    context.app.page.close_window()
    # print(context.original_window)


@then('Return to original window')
def switch_to_original_window(context):
    context.app.page.switch_to_window(context.original_window)


@then('Verify Google Play Target page opened')
def verify_play_window_opened(context):
    context.app.partner_page.verify_google_play_opened()


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
