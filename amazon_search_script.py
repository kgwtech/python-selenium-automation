import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

"""Path to Chromedriver Executable"""
driver_path = ChromeDriverManager().install()

"""Chrome Browser Instance"""
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

"""Open URL"""
driver.get("https://www.amazon.com/ref=nav_logo")
time.sleep(10)

"""Find search box and enter text"""
search_field = driver.find_element(By.ID, "twotabsearchtextbox")
search_field.send_keys("Men's body wash")

search_button = driver.find_element(By.ID, "nav-search-submit-button")
search_button.click()

expected_result = '"mug"'
# pulls the visible text from element
actual_result = driver.find_element(By.XPATH, "//span[@class='a-color-state a-text-bold']").text

assert expected_result == actual_result, "Error. Expected text did not equal actual text"
print("Test Case Passed.")

time.sleep(2)

driver.quit()
