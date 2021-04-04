from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
import time


class Product(Page):
  ADD_TO_CART= (By.NAME,"add-to-cart")
  CART_ICON = (By.CSS_SELECTOR,"span[class='cart-icon image-icon']")
  PRODUCT_PRICE=(By.XPATH,"//div[@class='price-wrapper']/descendant::span")
  PROD_DESC = (By.XPATH,"//li[@id='tab-title-description']//a")
  PROD_TEXT = (By.XPATH,"//a[@class='plain']//h1")
  NEXT_IMAGE = (By.XPATH,"//button[@aria-label='Next']")
 # NEXT_IMAGE = (By.XPATH,"")
  IMAGE_COUNT = (By.XPATH,"//img[@width='600']")
  def click_on_add_to_cart(self):
      self.click(*self.ADD_TO_CART)

  def click_on_cart_icon(self):
      self.click(*self.CART_ICON)

  def verify_prod_price(self):
      el= self.find_element(*self.PRODUCT_PRICE)
      assert el.text

  def verify_prod_desc(self):
      text ='DESCRIPTION'
      self.verify_text(text,*self.PROD_DESC)

  def prod_text(self):
      return self.find_element(*self.PROD_TEXT).text

  def click_on_next_image_button(self):
      self.wait_for_element_appear(*self.IMAGE_COUNT)
      ele= self.find_elements(*self.IMAGE_COUNT)
      for i in range(len(ele)):
       self.click(*self.NEXT_IMAGE)
       time.sleep(1)
