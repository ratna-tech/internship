from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.support import expected_conditions as EC

class Product(Page):
  ADD_TO_CART= (By.NAME,"add-to-cart")
  CART_ICON = (By.CSS_SELECTOR,"span[class='cart-icon image-icon']")
  PRODUCT_PRICE=(By.XPATH,"//div[@class='price-wrapper']/descendant::span")
  PROD_DESC = (By.XPATH,"//li[@id='tab-title-description']//a")
  PROD_TEXT = (By.XPATH,"//a[@class='plain']//h1")
  NEXT_IMAGE = (By.XPATH,"//button[@aria-label='Next']")
  IMAGE_COUNT = (By.XPATH,"//img[@width='600']")
  SORT_DROPDOWN = (By.CSS_SELECTOR,'select.orderby')
  PROD_STAR_RATING = (By.XPATH, "//div[@class='price-wrapper']//div")
  PRODUCT_PAGES = (By.CSS_SELECTOR,'ul.page-numbers>li')
  ICON_PREVIOUS_PAGE = (By.CSS_SELECTOR,'i.icon-angle-left')
  ICON_NEXT_PAGE =(By.CSS_SELECTOR,'i.icon-angle-right')
  QUICK_VIEW_OPEN = (By.CSS_SELECTOR, "a.quick-view ")
  QUICK_VIEW_CLOSE = (By.CSS_SELECTOR, "button.mfp-close")
  HOVER_OVER= (By.CSS_SELECTOR,"div.image-fade_in_back")
  flocator= [HOVER_OVER,QUICK_VIEW_OPEN]


  def open_orderby_rating_page(self):
      self.open_page('shop/?orderby')

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
        self.wait_for_element_click(*self.NEXT_IMAGE)
        time.sleep(1)

  def sort_products_by_average_rating(self):
      select =Select(self.find_element(*self.SORT_DROPDOWN))
      select.select_by_value('rating')


  def verify_star_rating(self):
      prod_rating = self.find_element(*self.PROD_STAR_RATING)
      assert 'Rated' in prod_rating.text, f'Expected prod_rating ,but got nothing'

  def click_through_product_pages(self):
      pages = self.find_elements(*self.PRODUCT_PAGES)
      for i in range(len(pages)-1):
          pages[i].click()
      Licons = self.wait_for_elements_appear(*self.ICON_PREVIOUS_PAGE)
      for icon in Licons:
          icon.click()
      Ricons = self.wait_for_elements_appear(*self.ICON_NEXT_PAGE)
      for icon in Ricons:
          icon.click()

  def verify_quick_viewopen_close(self):
      self.hover(*self.HOVER_OVER)
      self.click(*self.QUICK_VIEW_CLOSE)

  def verify_quick_view_add_to_cart(self):
      self.hover(*self.HOVER_OVER)
      self.wait_for_element_click(*self.ADD_TO_CART)

  def click_through_product_pages_by_clicking_12(self):
      pages = self.find_elements(*self.PRODUCT_PAGES)
      for i in range(len(pages)-1):
          pages[i].click()

  def click_through_product_pages_using_angle(self):
      pages = self.find_elements(*self.PRODUCT_PAGES)
      Licons = self.wait_for_elements_appear(*self.ICON_PREVIOUS_PAGE)
      for icon in Licons:
       icon.click()
      Ricons = self.wait_for_elements_appear(*self.ICON_NEXT_PAGE)
      for icon in Ricons:
           icon.click()





