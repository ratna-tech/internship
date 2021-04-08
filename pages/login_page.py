from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time

class LoginPage(Page):
    EMAIL_HEADING = (By.XPATH,"//label[@for='username']")
    EMAIL_TEXTBOX = (By.ID,'username')
    PASSWORD_HEADING =(By.CSS_SELECTOR,"label[for='password']")
    PASSWORD_TEXTBOX = (By.ID,'password')
    REMEMBERME_TEXT = (By.CSS_SELECTOR,'label.woocommerce-form__label-for-checkbox>span')
    REMEMBERME_CHECKBOX = (By.ID,'rememberme')
    LOGIN_BUTTON =(By.CSS_SELECTOR,'button.woocommerce-button ')
    LOST_PASSWORD = (By.CSS_SELECTOR,'p.lost_password>a')
    FOOTER_BLOCKS = (By.CSS_SELECTOR,'span.widget-title')
    FOOTER_LIST =['BEST SELLING','LATEST','TOP RATED']


    def open_login_page(self):
        self.open_page('my-account/')

    def verify_email_heading(self,search_word):
        self.verify_text(search_word,*self.EMAIL_HEADING)

    def verify_email_textbox(self):
       assert self.find_element(*self.EMAIL_TEXTBOX),f'Expected email text box,got nothing'

    def verify_password_heading(self,search_word):
        self.verify_text(search_word,*self.PASSWORD_HEADING)

    def verify_password_textbox(self):
        assert self.find_element(*self.PASSWORD_TEXTBOX),f'Expected password text box,got nothing'

    def verify_rememberme_text(self,search_text):
        self.verify_text(search_text,*self.REMEMBERME_TEXT)

    def verify_rememberme_checkbox(self):
        assert self.find_element( *self.REMEMBERME_CHECKBOX),f'Expected Remember me checkbox box,got nothing'

    def verify_loginbutton(self,search_word):
        self.verify_text(search_word,*self.LOGIN_BUTTON)

    def verify_lost_password_link(self):
        self.click(*self.LOST_PASSWORD)
        current_url = self.driver.current_url
        assert 'lost-password' in current_url,f'Expected lost-password, but got {current_url}'

    def verify_footer_blocks(self):
        el= self.find_elements(*self.FOOTER_BLOCKS)
        for i in range(len(el)):
            assert el[i].text == self.FOOTER_LIST[i]