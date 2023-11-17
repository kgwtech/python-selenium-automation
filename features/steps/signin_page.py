from selenium.webdriver.common.by import By
from behave import given, when, then
from time import sleep


@when('Click Sign In button')
def access_signin(context):
    signin_btn_1 = context.driver.find_element(By.XPATH, "//span[text()='Sign in']")
    signin_btn_1.click()
    context.driver.find_element(By.XPATH, "//a[@data-test='accountNav-signIn']").click()


@then('Verify Sign In form opened')
def verify_access(context):
    expected_text = context.driver.find_element(By.CSS_SELECTOR, "h1[class*=AuthHeading]").text
    assert "Sign into your Target account" in expected_text, f"Expected text not in {expected_text}"
