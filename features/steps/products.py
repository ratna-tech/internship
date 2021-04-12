from behave import given, when, then

@given('open all products page')
def open_all_products_page(context):
    context.app.products.open_orderby_rating_page()

@when('sort products by average rating')
def sort_products_by_average_rating(context):
    context.app.products.sort_products_by_average_rating()

@then('1st product has rating stars displayed after sorting')
def first_product_has_rating_stars(context):
    context.app.products.verify_star_rating()

@then('User can click through product pages after sorting is done')
def click_through_product_pages(context):
    context.app.products.click_through_product_pages()

@then('User can open and close Quick View by clicking on closing X')
def open_close_quickview(context):
    context.app.products.verify_quick_viewopen_close()

@then('User can click Quick View and add product to cart')
def add_tocart_quickview(context):
    context.app.products.verify_quick_view_add_to_cart()

@then('User can click trough multiple product pages by clicking 1, 2 for page number')
def click_through_page_12(context):
    context.app.products.click_through_product_pages_by_clicking_12()

@then('User can click trough multiple product pages by clicking > and <')
def click_through_page_using_arrow(context):
    context.app.products.click_through_product_pages_using_angle()