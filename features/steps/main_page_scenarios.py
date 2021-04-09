from selenium.webdriver.common.by import By
from behave import given, when, then
import time

CATEGORY_LIST=['ACCESSORIES','IPAD','IPHONE','MACBOOK']
CATEGORY_LIST2=['HOME / ACCESSORIES','HOME / IPAD','HOME / IPHONE','HOME / MACBOOK']
cart_message='No products in the cart.'


@given('Open GetTop page')
def open_GetTop(context):
    context.app.main_page.open_main_page()

@then("text {search_word} is shown")
def verify_text(context,search_word):
   context.app.main_page.verify_header_text(search_word)

@then("Verify sale icon is visible")
def verify_text(context):
    context.app.main_page.verify_sale_icon()

@then("Verify product name is displayed")
def verify_prod_text(context):
    context.app.main_page.verify_prod_name()

@then("Verify product category is displayed")
def verify_category_text(context):
    context.app.main_page.verify_prod_category()


@then("Verify image is displayed")
def verify_image(context):
    context.app.main_page.verify_prod_image()

@then("Verify price is displayed")
def verify_price(context):
    context.app.main_page.verify_prod_price()

@then("verify star rating is displayed")
def verify_star_rating(context):
    context.app.main_page.verify_star_rating()

@when('Hover over and click on heart icon to add to wish list')
def click_on_heart_icon(context):
    context.app.main_page.hover_over_and_click_heart_icon()


@when('Click on heart icon to go to wish list page')
def go_to_wishlist_page(context):
    context.app.main_page.click_on_heart_icon()

@then('verify product appears in wish list page')
def verify_prod_inwishlist_page(context):
    context.app.wish_list.verify_product_text()

@when('Click on a product from LATEST PRODUCTS ON SALE section')
def click_on_sale_prod(context):
    global search_text
    search_text = context.app.main_page.sale_prod_text()
    print(search_text)
    context.app.main_page.click_on_sale_prod()

@when('Click on ADD TO CART')
def click_on_add_to_cart(context):
    context.app.products.click_on_add_to_cart()

@when('Click on cart icon')
def click_on_cart_icon(context):
    context.app.products.click_on_cart_icon()
    time.sleep(5)

@then('verify item appears in cart')
def verify_item_in_cart(context):
 context.app.carts.verify_product_text(search_text)

@then('Verify product price shown')
def verify_prod_price(context):
    context.app.products.verify_prod_price()

@then('verify product description shown')
def verify_prod_desc(context):
  context.app.products.verify_prod_desc()

@when('Click on quick view')
def click_on_quick_view(context):
  #context.app.main_page.hover_over()
  context.app.main_page.click_on_quick_view()

@then('verify quick view opens')
def verify_quick_view(context):
  context.app.main_page.verify_quick_view()
  time.sleep(3)

@then('verify quick view closes when X is clicked')
def verify_quick_view_close(context):
  context.app.main_page.verify_quick_view_close()

@when('hover over product and click on quick view')
def hover_over_prod(context):
    context.app.main_page.hover_over()

@then('verify item added message appears in main page')
def item_added_message(context):
    message= context.app.main_page.prod_added_incart_message()
    context.app.main_page.get_prod_text_and_verify(message)

@then('Click through product images')
def click_on_next_button(context):
    context.app.products.click_on_next_image_button()

@then('Verify Correct categories under Browse section is displayed')
def verify_browse_category(context):
 context.app.main_page.verify_browse_category(CATEGORY_LIST)

@then('Click on categories under browse and verify correct page opens')
def click_on_categories(context):
    context.app.main_page.click_on_categories(CATEGORY_LIST2)

@when('Hover over Carts icon')
def hover_over_cart(context):
    context.app.main_page.hover_over_cart()

@then('verify products can be removed from wish list')
def verify_wishlist_removed(context):
    context.app.main_page.remove_from_wishlist()

@given('Open wishlist page')
def open_wishlist_page(context):
    context.app.main_page.open_wishlist_page()

@then('verify {WISHLIST_MESSAGE} message')
def verify_noprod_added_message_wishlistpage(context,WISHLIST_MESSAGE):
    context.app.main_page.verify_noprod_added_message_wishlistpage(WISHLIST_MESSAGE)



