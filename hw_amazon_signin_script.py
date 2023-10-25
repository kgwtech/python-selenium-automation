"""Create a test case for the Sign In page using python & selenium script.
(Make sure to use Incognito browser mode when searching for locators)"""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.maximize_window()
driver.get("https://www.amazon.com/")

# Needed to manually type Amazon.com captcha for "Human Verification"
time.sleep(10)

orders_btn = driver.find_element(By.ID, "nav-orders")
orders_btn.click()

expected_result = "Sign in"
actual_result = (
    driver.find_element(By.XPATH,
                        "//div[@class='a-box-inner a-padding-extra-large']//h1[@class='a-spacing-small']").text)

assert expected_result == actual_result, f"Expected result {expected_result}, but got {actual_result}"
print("Test Case Passed.")

time.sleep(2)

driver.quit()
