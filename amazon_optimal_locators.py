from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# init driver
driver_path = ChromeDriverManager().install()
driver = webdriver.Chrome(service=Service(driver_path))
driver.maximize_window()

# collapse url into variable & open webpage
amazon_url = ("https://www.amazon.com/ap/register?showRememberMe=true&openid.pape.max_auth_age=0&openid.return_to"
              "=https%3A%2F%2Fwww.amazon.com%2F%3Fref_%3Dnav_custrec_signin&prevRID=GWQHHZQFY6XX0STSN884&openid"
              ".identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=usflex"
              "&openid.mode=checkid_setup&prepopulatedLoginId=&failedSignInCount=0&openid.claimed_id=http%3A%2F"
              "%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&pageId=usflex&openid.ns=http%3A%2F%2Fspecs.openid"
              ".net%2Fauth%2F2.0")
driver.get(amazon_url)

# Best locator for amazon button is css_selector w/classes.
# Unique id is unavailable, css_selector is more ideal than xpath
amazon_btn = driver.find_element(By.CSS_SELECTOR, ".a-icon.a-icon-logo")

# Best locator for "Create account" text is css_selector w/ tag.
# Unique id is unavailable, css_selector is more ideal than xpath
create_acct_text = driver.find_element(By.CSS_SELECTOR, "h1.a-spacing-small")

# Best locator for name field is ID.
# Unique id is available
name_field = driver.find_element(By.ID, "ap_customer_name")

# Best locator for email field is ID.
# Unique id is available
email_field = driver.find_element(By.ID, "ap_email")

# Best locator for password field is ID.
# Unique id available
password_field = driver.find_element(By.ID, "ap_password")

# Best locator for re-enter pass field is ID.
# Unique id available
repass_field = driver.find_element(By.ID, "ap_password_check")

# Best locator for create account button is ID.
# Unique id available
continue_btn = driver.find_element(By.ID, "continue")

# Best locator for conditions link is Xpath w/text.
# Unique id unavailable
conditions_link = driver.find_element(By.XPATH, "//a[text()='Conditions of Use']")

# Best locator for privacy notice link is Xpath w/text.
# Unique id unavailable
privacy_link = driver.find_element(By.XPATH, "//a[text()='Privacy Notice']")

# Best locator for sign in link is css_selector w/classes.
# Unique id is unavailable, css_selector is more ideal than xpath
signin_link = driver.find_element(By.CSS_SELECTOR, ".a-link-emphasis")



