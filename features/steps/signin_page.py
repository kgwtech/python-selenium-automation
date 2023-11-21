from selenium.webdriver.common.by import By
from behave import *

""" Calls methods from the Page Object for Webpage under test """


@then('Verify Sign In form opened')
def verify_signin_form_opened(context):
    context.app.signin_page.verify_page_opened()
