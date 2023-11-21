from behave import *

""" Calls methods from the Page Object for Webpage under test """


@then("Verify “Your cart is empty” message is shown")
def verify_empty_cart_msg(context):
    context.app.cart_page.verify_empty_cart_msg()
