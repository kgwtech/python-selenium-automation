from behave import *

""" Calls methods from the Page Object for Webpage under test """


@when("Click on Cart icon")
def click_cart_icon(context):
    context.app.cart_page.click_icon_from_main()


@then("Verify “Your cart is empty” message is shown")
def verify_empty_cart_msg(context):
    context.app.cart_page.verify_empty_cart_msg()
