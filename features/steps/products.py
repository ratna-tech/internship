from behave import given, when, then

@given('open order by rating page')
def open_orderby_rating_page(context):
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