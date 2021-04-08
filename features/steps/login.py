from behave import given, when, then

@given('opens login page')
def open_login_page(context):
    context.app.login_page.open_login_page()

@then('verify email header {} present')
def verify_email_heading(context,search_word):
    context.app.login_page.verify_email_heading(search_word)

@then('verify email textbox present')
def verify_email_textbox(context):
    context.app.login_page.verify_email_textbox()

@then('verify password header {} present')
def verify_password_heading(context,search_word):
    context.app.login_page.verify_password_heading(search_word)

@then('verify password textbox present')
def verify_password_textbox(context):
    context.app.login_page.verify_password_textbox()

@then('verify header {} present')
def verify_rememberme_text(context,search_text):
    context.app.login_page.verify_rememberme_text(search_text)

@then('verify Remember me checkbox present')
def verify_rememberme_checkbox(context):
    context.app.login_page.verify_rememberme_checkbox()

@then('verify Lost your password link present')
def verify_lost_password_linktext(context):
    context.app.login_page.verify_lost_password_link()

@then('verify {} button present')
def verify_rememberme_text(context,search_text):
    context.app.login_page.verify_loginbutton(search_text)

@then('verify User can see Best Selling, Latest, Top Rated blocks')
def verify_footer_blocks(context):
    context.app.login_page.verify_footer_blocks()