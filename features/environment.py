from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from app.application import Application
#from support.logger import logger
def browser_init(context,test_name):
    """
    :param context: Behave context
    :param test_name = scenario.name
    """
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\Ratna Sinha\Desktop\internship\chromedriver.exe")
    #context.driver = webdriver.Chrome(executable_path=r'C:\Users\Ratna Sinha\Desktop\GITHUB\jobeasy-automation\python-selenium-automation\chromedriver.exe')
    # context.driver = webdriver.Safari()
    # context.driver = webdriver.Firefox()
   # desired_cap ={
  #     'browser': 'Chrome',
   #     'browser_version': '87',
    #    'os': 'Windows',
    #    'os_version': '10',
    #    'name':test_name
    #}
    #bs_uname = 'ratnasinha1'
    #s_key= 'ihgMiyt447DpNbhbAHuG'
  #  url = f'http://{bs_uname}:{bs_key}@hub-cloud.browserstack.com/wd/hub'
  #  context.driver = webdriver.Remote(url,desired_capabilities=desired_cap)
    context.driver.maximize_window()
    context.driver.implicitly_wait(4)
    context.driver.wait = WebDriverWait(context.driver, 20)
    context.app = Application(context.driver)

def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
   # logger.info(f'started scenario:{scenario.name}')
    browser_init(context,scenario.name)


def before_step(context, step):
    print('\nStarted step: ', step)
  #  logger.info(f'started step:{step}')

def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)
    #    logger.error(f'failed step: {step}')


def after_scenario(context, feature):
    context.driver.delete_all_cookies()
    context.driver.quit()
