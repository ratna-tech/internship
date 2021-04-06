from selenium.webdriver.common.by import By
from pages.base_page import Page
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
class Main_Page(Page):
  HEADER_TEXT= (By.XPATH,"//span[@class='section-title-main'][1]")
  HEART_ICON = (By.XPATH,"//i[@class='icon-heart']")
  SALE_PROD = (By.XPATH,"//div[@class='image-fade_in_back']")
  SALE_PROD_TEXT= (By.XPATH,"//p[@class='name product-title']//a")
  QUICK_VIEW = (By.XPATH,"//a[@class='quick-view quick-view-added']")
  QUICK_VIEW_OPEN = (By.XPATH,"//span[@class='woocommerce-Price-amount amount']")
  QUICK_VIEW_CLOSE= (By.XPATH,"//button[@class='mfp-close']")
  PROD_INCART_TEXT = (By.XPATH,"//div[@class='message-container container success-color medium-text-center']")
  SALE_ICON=(By.XPATH,"//span[@class='onsale']")
  PROD_NAME =(By.XPATH,"//p[@class='name product-title']")
  PROD_CATEGORY =(By.XPATH,"//p[@class='category uppercase is-smaller no-text-overflow product-cat op-7']")
  PROD_IMAGE =(By.XPATH,"//div[@class='image-fade_in_back']//a")
  PROD_PRICE=(By.XPATH,"//span[@class='price']//descendant::ins//span//span")
  PROD_STAR_RATING = (By.XPATH,"//div[@class='price-wrapper']//div")
  NUM_PROD_ON_SALE =(By.XPATH,"//div[@class='product-small box ']")
  PROD_ON_WISH_PAGE = (By,"//td[@class='product-name']//a")
  CHECK_WISHLIST_ADDED= (By.CSS_SELECTOR,'div.yith-wcwl-add-to-wishlist>div')
  flocator =[SALE_PROD,QUICK_VIEW]
  BROWSE_CATEGORY = (By.XPATH,"//div//h5")
  BROWSE_CATEGORY2 = (By.XPATH, "//div//h5[2]")
  CATEGORY_LIST=['Accessories','iPad','iPhone','MacBook']
  CATEGORY_TEXT =(By.CSS_SELECTOR,'nav.woocommerce-breadcrumb')

  def open_main_page(self):
      self.open_page('')

  def verify_header_text(self,search_word):
      self.verify_text(search_word,*self.HEADER_TEXT)

  def verify_sale_icon(self):
      sale_text=self.find_elements(*self.SALE_ICON)
      num_prod_on_sale =self.find_elements(*self.NUM_PROD_ON_SALE)
      assert len(sale_text) == len(num_prod_on_sale),f'Expected {len(num_prod_on_sale)}of sale icon,but got {len(sale_text)}'
      for i in range(len(sale_text)):
          print(sale_text[i].text)
          assert sale_text[i].text == 'Sale!', f'Expected {sale_text[i].text} , but got nothing'

  def verify_prod_name(self):
      prod_name=self.find_elements(*self.PROD_NAME)
      num_prod_on_sale = self.find_elements(*self.NUM_PROD_ON_SALE)
      assert len(prod_name) == len(num_prod_on_sale), f'Expected {len(num_prod_on_sale)}of product name,but got {len(prod_name)}'
      for i in range(len(prod_name)):
          print(prod_name[i].text)
          assert prod_name[i].text != 0, f'Expected {prod_name[i].text} , but got nothing'

  def verify_prod_category(self):
      prod_category = self.find_elements(*self.PROD_CATEGORY)
      num_prod_on_sale = self.find_elements(*self.NUM_PROD_ON_SALE)
      assert len(prod_category) == len(num_prod_on_sale), f'Expected {len(num_prod_on_sale)}of product category,but got {len(prod_category)}'
      for i in range(len(prod_category)):
          print(prod_category[i].text)
          assert prod_category[i].text != 0, f'Expected prod_category , but got nothing'

  def verify_prod_image(self):
      prod_image = self.find_elements(*self.PROD_IMAGE)
      num_prod_on_sale = self.find_elements(*self.NUM_PROD_ON_SALE)
      assert len(prod_image) == len(num_prod_on_sale), f'Expected {len(num_prod_on_sale)}of product images,but got {len(prod_image)}'
      for i in range(len(prod_image)):
          print(prod_image[i].get_attribute('href'))
          assert 'https://gettop.us/product'in prod_image[i].get_attribute('href'),f'Expected prod_image,but got nothing'

  def verify_prod_price(self):
      prod_price = self.find_elements(*self.PROD_PRICE)
      num_prod_on_sale = self.find_elements(*self.NUM_PROD_ON_SALE)
      assert len(prod_price) == len(num_prod_on_sale), f'Expected {len(num_prod_on_sale)}of product price,but got {len(prod_price)}'
      for i in range(len(prod_price)):
          print(prod_price[i].text)
          assert prod_price[i].text != 0, f'Expected prod_price , but got nothing'

  def verify_star_rating(self):
      prod_rating = self.find_elements(*self.PROD_STAR_RATING)
      num_prod_on_sale = self.find_elements(*self.NUM_PROD_ON_SALE)
      assert len(prod_rating) == len(num_prod_on_sale), f'Expected {len(num_prod_on_sale)}of product ratings,but got {len(prod_rating)}'
      for i in range(len(prod_rating)):
          print(prod_rating[i].text)
          assert 'Rated' in prod_rating[i].text, f'Expected prod_rating , but got nothing'

  def click_on_heart_icon(self):
      self.find_element(*self.HEART_ICON)

  def Click_on_heart_icon_to_go_to_wish_list_page(self):
      self.click(*self.HEART_ICON)

  def verify_product_appears_in_wish_list_page(self):

      pass
  def click_on_sale_prod(self):
      self.click(*self.SALE_PROD)

  def sale_prod_text(self):
      return self.find_element(*self.SALE_PROD_TEXT).text

  def click_on_quick_view(self):
      self.click(*self.QUICK_VIEW)
      time.sleep(8)

  def verify_quick_view(self):
      self.find_element(*self.QUICK_VIEW_OPEN)

  def verify_quick_view_close(self):
      self.click(*self.QUICK_VIEW_CLOSE)

  def hover_over(self):
    self.hover(*self.flocator)
    #item_tab =self.find_element(*self.SALE_PROD)
    #actions = ActionChains(self.driver)
    #actions.move_to_element(item_tab)
    #actions.click(self.find_element(*self.QUICK_VIEW))
    #actions.perform()
    #from time import sleep
    #sleep(1)

  def hover_over_and_click_heart_icon(self):
    item_tab =self.find_element(*self.SALE_PROD)
    actions = ActionChains(self.driver)
    actions.move_to_element(item_tab)
    actions.click(self.find_element(*self.HEART_ICON))
    actions.click(self.find_element(*self.HEART_ICON))
    actions.perform()
    from time import sleep
    sleep(2)

  def prod_added_incart_message(self):
      return self.find_element(*self.PROD_INCART_TEXT).text

  def get_prod_text_and_verify(self,search_word):
      self.verify_partial_text(search_word, *self.SALE_PROD_TEXT)

  def verify_browse_category(self,CATEGORY_LIST):
      categories= self.find_elements(*self.BROWSE_CATEGORY)

      for i in range(len(CATEGORY_LIST)):
          assert CATEGORY_LIST[i] == categories[i].text,f'Expected {CATEGORY_LIST[i]} but got{categories[i].text}'

  def click_on_categories(self,CATEGORY_LIST):
      names = []
      LINKS = self.find_elements(*self.BROWSE_CATEGORY)

      for i in range(len(LINKS)):
       LINKS = self.find_elements(*self.BROWSE_CATEGORY)
       LINKS[i].click()
       page_name = self.find_element(*self.CATEGORY_TEXT)
       names.append(page_name.text)
       print(names)
       self.driver.back()

      for i in range(len(CATEGORY_LIST)):
        print(names[i])
        assert names[i] in CATEGORY_LIST, f'Expected {CATEGORY_LIST[i]} , but got {names[i]}'




