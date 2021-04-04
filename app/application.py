from pages.main_page import Main_Page
from pages.wish_list import WishList
from pages.carts import CartsPage
from pages.products import Product
#from pages.order_cancel import OrderCancel
class Application:
    def __init__(self, driver):
        self.driver = driver
        self.main_page = Main_Page(self.driver)
        self.carts = CartsPage(self.driver)
        self.products  = Product(self.driver)
        self.wish_list= WishList(self.driver)