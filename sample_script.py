from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

# waits up to amount of time provided
# works for all find_element() and find_elements()
# checks every 100ms for element presence
# placed in code only once, for all find_element() and find_elements()
# if fails, no exception error will show
driver.implicitly_wait(5)
driver.wait = WebDriverWait(driver, 10)


# def explicit wait
# when explicit wait is used, waits up to timeout time for expected conditions
# checks for expected conditions every 500 ms
# driver.wait.until(EC.presence_of_element_located())

# open the url
driver.get('https://www.google.com/')

# populate search field
search = driver.find_element(By.NAME, 'q')
search.clear()
search.send_keys('1017 Alyx 9sm')


# click search button
driver.find_element(By.NAME, 'btnK').click()

# verify search results
assert '1017 Alyx 9sm' in driver.current_url.lower(), f"Expected query not in {driver.current_url.lower()}"
print('Test Passed')

driver.quit()
