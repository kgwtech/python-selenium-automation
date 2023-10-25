"""Practice with locators.
Create locators + search strategy for these page elements of Amazon"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

# Amazon logo
driver.find_element(By.XPATH, "//i[@class='a-icon a-icon-logo']")

# Email field
driver.find_element(By.ID, "ap_email")

# Continue button
driver.find_element(By.XPATH, "//input[@id='continue']")

# Conditions of use link,
driver.find_element(By.XPATH, "//div[@id='legalTextRow']//a[contains(text(),'Conditions of Use')]")

# Privacy Notice link,
driver.find_element(By.XPATH,"//div[@id='legalTextRow']//a[contains(text(),'Privacy Notice')]")

# Need help link
driver.find_element(By.XPATH, "//span[@class='a-expander-prompt']")

# Forgot your password link
driver.find_element(By.ID, "auth-fpp-link-bottom")

# Other issues with Sign-In link
driver.find_element(By.ID, "ap-other-signin-issues-link")

# Create your Amazon account button
driver.find_element(By.ID, "createAccountSubmit")

