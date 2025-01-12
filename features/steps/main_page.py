from behave import *

""" Calls methods from the Page Object for Webpage under test """


@given('Open target main page')
def open_target(context):
    context.app.main_page.open_main()


@when("Click on Cart icon")
def click_cart_icon(context):
    context.app.main_page.click_cart_icon()


@when('Search for {product}')
def search_product(context, product):
    context.app.main_page.search(product)


@when('Click Sign In')
def click_sign_in(context):
    context.app.main_page.click_signin()


@when('Hover over signin button')
def hover_signin_button(context):
    context.app.main_page.hover_over_signin()


@then('Verify Signin arrow shown')
def verify_verify_signin_arrow_shown(context):
    context.app.main_page.verify_signin_arrow_shown()


@then('Navigate to Circle page')
def navigate_circle(context):
    context.app.main_page.nav_to_circle_page()


@then('From right side navigation menu, click Sign In')
def click_sign_in_from_nav(context):
    context.app.main_page.signin_from_nav()


@then('Verify header is present')
def verify_header_preset(context):
    context.app.main_page.verify_header()


@then('Verify header has {number} links')
def verify_header_has_links(context, number):
    context.app.main_page.verify_header_links()

