from behave import given, when, then


@when('Login')
def login(context):
    context.app.login_page.login()


@then('Verify that user logged in')
def verify_login(context):
    context.app.login_page.verify_login()

