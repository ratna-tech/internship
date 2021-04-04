from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

class Page:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 15)
        self.base_url = 'https://gettop.us/'

    def click(self, *locator):
        self.driver.find_element(*locator).click()


    def find_element(self, *locator):
        return self.driver.find_element(*locator)
        #return self.driver.wait.until(EC.presence_of_element_located(*locator))

    def find_elements(self, *locator):
        return self.driver.find_elements(*locator)

    def open_page(self, url=''):
        #self.driver.get(url)
        self.driver.get(f'{self.base_url}{url}')

    def input_text(self, text: str, *locator):
        e= self.driver.find_element(*locator)
        #e = self.driver.wait.until((EC.presence_of_element_located(*locator)))
        e.clear()
        e.send_keys(text)

    def wait_for_element_click(self, *locator):
        e = self.wait.until(EC.element_to_be_clickable(locator))
        e.click()

    def wait_for_element_disappear(self, *locator):
        self.wait.until(EC.invisibility_of_element(locator))

    def wait_for_element_appear(self, *locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def verify_text(self, expected_text: str, *locator):
        """
        Search for a webelement, get its text, compare with expected_text
        :param expected_text: Text to be in webelement
        :param locator: Search strategy and locator of webelemnt (ex. (By.ID, 'id') )
        """
        e = self.driver.find_element(*locator)
        actual_text = e.text
        assert expected_text == actual_text, f"Expected {expected_text} does not match actual {actual_text}"

    def verify_partial_text(self, expected_text: str, *locator):
        e = self.driver.find_element(*locator)
        actual_text = e.text
        assert actual_text in expected_text , f"Expected {expected_text} does not match actual {actual_text}"

    #def hover(self,*flocator, *clocator):
       # item_tab = self.find_element(*self.flocator)
       # actions = ActionChains(self.driver)
       # actions.move_to_element(item_tab)
        #actions.click(self.find_element(*self.clocator))
       # actions.perform()
       # from time import sleep
       # sleep(5)