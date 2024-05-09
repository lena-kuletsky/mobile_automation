from behave import given, when, then


@when('Tap on the Avatar in the top-left corner')
def tap_avatar(context):
    context.app.logout_page.tap_avatar()


@when('Tap on ‘Settings’ from side menu')
def tap_settings(context):
    context.app.logout_page.tap_settings()


@when('Tap on ‘Logout’ button')
def tap_logout(context):
    context.app.logout_page.tap_logout()


@when('Confirm logout, tap on Yes')
def tap_yes_btn(context):
    context.app.logout_page.tap_yes_btn()


@then('Verify that user logged out')
def verify_logout(context):
    context.app.logout_page.verify_logout()
