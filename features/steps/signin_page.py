from selenium.webdriver.common.by import By
from behave import *

""" Calls methods from the Page Object for Webpage under test """


@given('Open target sign in page')
def open_signin_page(context):
    context.app.signin_page.open_signin_page()


@then('Click on Target terms and conditions link')
def click_terms_conditions(context):
    context.app.signin_page.click_terms_conditions()


@then('User can close new window and switch back to original')
def close_and_switch_window(context):
    context.app.page.close_window()
    context.app.page.switch_to_window(context.original_window)


@then('Input {email} and {password} on SignIn page')
def enter_credentials(context, email, password):
    context.app.signin_page.input_credentials(username=email, password=password)


@then('Click Sign In')
def login(context):
    context.app.signin_page.login()


@then('Verify user is successfully logged in')
def verify_successful_login(context):
    context.app.signin_page.verify_login()


@then("Verify that {error_msg} message is shown")
def verify_login_error_msg(context, error_msg):
    context.app.signin_page.verify_login_error_msg(error_msg)


@then('Verify Sign In form opened')
def verify_signin_form_opened(context):
    context.app.signin_page.verify_page_opened()


@then('Verify Terms and Conditions page is opened')
def verify_conditions_page_opened(context):
    context.app.partner_page.verify_terms_conditions_opened()
