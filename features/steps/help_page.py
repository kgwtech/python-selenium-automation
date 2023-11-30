from behave import *

""" Calls methods from the Page Object for Webpage under test """


@given('Open target help page')
def open_help_page(context):
    context.app.help_page.open_help_page()


@given('Open target help page for returns')
def open_help_return_page(context):
    context.app.help_page.open_help_return_page()


@when('Select Help topic {topic}')
def select_promotions_coupons(context, topic):
    context.app.help_page.select_topic(topic)


@then("Verify 'Target Help' text")
def verify_help_header_text(context):
    context.app.help_page.verify_help_header_text()


@then('Enter {help_search} in text field')
def enter_text(context, help_search):
    context.app.help_page.search(help_search)


@then('Click search icon button')
def verify_search_icon(context):
    context.app.help_page.click_search_btn()


@then('Verify options box has {number_1} boxes and {number_2} grid box')
def verify_option_boxes(context, number_1, number_2):
    context.app.help_page.verify_option_boxes(number_1, number_2)


@then('Verify additional resources box has {number} boxes')
def verify_resource_boxes(context, number):
    context.app.help_page.verify_resource_boxes(number)


@then("Verify 'Browse all Help pages' text")
def verify_browse_text(context):
    context.app.help_page.verify_browse_pages_text()


@then('Verify Returns page opened')
def verify_return_page_opened(context):
    context.app.help_page.verify_return_page_opened()


@then('Verify Current promotions page opened')
def verify_promotions_page_opened(context):
    context.app.help_page.verify_promotions_opened()


@then('Verify Technical Support page opened')
def verify_tech_supp_page_opened(context):
    context.app.help_page.verify_tech_supp_page_opened()
