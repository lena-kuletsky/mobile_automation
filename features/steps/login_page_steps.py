from behave import given, when, then


@given('Login')
def login(context):
    context.app.login_page.login()



