from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select


class WishList(Page):
  PROD_TEXT = (By.XPATH,"//td[@class='product-name']//a")
  REMOVE_WISHLIST =(By.CSS_SELECTOR,'a.remove')

  def open_wishlist_page(self):
      self.open_page('my-account/wishlist/')

  def verify_product_text(self):
      search_word =self.find_element(*self.PROD_TEXT).text
      self.verify_text(search_word,*self.PROD_TEXT)

  def remove_from_wishlist(self):
      el= self.find_elements(*self.REMOVE_WISHLIST)
      if len(el) > 0:
          for i in range(len(el)):
              self.click(*self.REMOVE_WISHLIST)