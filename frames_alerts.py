from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.alert import Alert

# init the driver
driver_path = ChromeDriverManager().install()
service = Service(driver_path)
driver = webdriver.Chrome(service=service)

driver.implicitly_wait(4)

# open the url
driver.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_iframe')

# Switch to frame 1
driver.switch_to.frame('iframeResult')

# Switch to frame 2
frame2 = driver.find_element(By.CSS_SELECTOR, "iframe[src='https://www.w3schools.com']")
driver.switch_to.frame(frame2)

menu = driver.find_element(By.CSS_SELECTOR, '.tnb-menu-btn')
print(menu.get_attribute('title'))

assert menu.get_attribute('title') == 'Menu', f"Title is {menu.get_attribute('title')} instead of Menu"

''' ALERTS '''

Alert(driver).accept()
Alert(driver).dismiss()

driver.quit()