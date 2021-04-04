from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class WishList(Page):
 # PROD_TEXT= (By.XPATH,"//p[@class='name product-title']/a[1]")
  PROD_TEXT = (By.XPATH,"//td[@class='product-name']//a")

  def open_main_page(self):
      self.open_page('my-account/wishlist/')

  def verify_product_text(self):
      search_word =self.find_element(*self.PROD_TEXT).text
      self.verify_text(search_word,*self.PROD_TEXT)