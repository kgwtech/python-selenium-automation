from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@given('Open target main page')
def open_target(context):
    context.driver.get('https://www.target.com/')


@when('Search for {product}')
def search_product(context, product):
    context.driver.find_element(By.ID, 'search').send_keys(product)
    context.driver.find_element(By.CSS_SELECTOR, "[data-test='@web/Search/SearchButton']").click()
    sleep(6)  # wait for ads to disappear


@then('Verify search worked for {expected_product}')
def verify_search(context, expected_product):
    search_results_header = context.driver.find_element(By.CSS_SELECTOR, "[data-test='resultsHeading']").text
    assert expected_product in search_results_header, f'Expected text coffee not in {search_results_header}'


@then('Verify {expected_url} search result url')
def verify_search_url(context, expected_url):
    assert expected_url in context.driver.current_url, \
        f"Expected {expected_url} not in {context.driver.current_url}"


@then('Verify header is present')
def verify_header_visible(context):
    context.driver.find_element(By.CSS_SELECTOR, "#utilityNav-registries")


@then('Verify header has {number} links')
def verify_header_links(context, number):
    number = int(number)
    links = context.driver.find_elements(By.CSS_SELECTOR, "[data-test*='@web/GlobalHeader/UtilityHeader/']")
    # always returns either an empty list of elements or a list of elements
    assert len(links) == number, f"Expected {links} links, but got {len(links)}"




