from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application


def browser_init(context, scenario_name):
    """
    :param context: Behave context
    """

    ''' CHROME BROWSER '''
    driver_path = ChromeDriverManager().install()
    service = Service(driver_path)
    context.driver = webdriver.Chrome(service=service)

    ''' HEADLESS '''
    # options = webdriver.ChromeOptions()
    # options.add_argument('headless')
    # service = Service(ChromeDriverManager().install())
    # context.driver = webdriver.Chrome(
    #     options=options,
    #     service=service
    # )

    ''' FIREFOX BROWSER '''
    #     service = Service(executable_path='/Users/prime./QA/python-selenium-automation/geckodriver')
    #     context.driver = webdriver.Firefox(service=service)

    ''' SAFARI BROWSER '''
    #     context.driver = webdriver.Safari()

    ''' BROWSERSTACK '''
    # email: telme0@btcmod.com
    # pass: fakepass123
    bs_user = 'telme_Jt8xpc'
    bs_key = 'bFfymLgkpVKb4t7iAK4T'
    url = f"https://{bs_user}:{bs_key}@hub-cloud.browserstack.com/wd/hub"

    options = Options()
    bstack_options = {
        'os': 'OS X',
        'osVersion': 'Ventura',
        'browserName': 'Chrome',
        'sessionName': scenario_name
    }
    options.set_capability('bstack:options', bstack_options)
    context.driver = webdriver.Remote(command_executor=url, options=options)

    ''' BROWSER TESTING __INIT__ '''
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, timeout=15)
    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context, scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
