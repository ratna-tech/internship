from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class CartsPage(Page):
  PROD_TEXT= (By.XPATH,"//td[3]//a")


  def verify_product_text(self,search_word):
      #search_word =self.find_element(*self.PROD_TEXT).text
      self.verify_text(search_word,*self.PROD_TEXT)