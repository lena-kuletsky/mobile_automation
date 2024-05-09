from behave import given, when, then


@when('Tap on ‘My Profile’ from the side menu')
def tap_my_profile(context):
    context.app.profile_page.tap_my_profile()


@when('Tap on ‘Takes’ tab')
def tap_takes_tab(context):
    context.app.profile_page.tap_takes_tab()


@when('Select post')
def select_post(context):
    context.app.profile_page.select_post()


@when('Tap on the three-dot button')
def tap_three_dot_button(context):
    context.app.profile_page.tap_three_dot_button()


@when('From the popup window that appears, tap on ‘Delete this post’ option')
def delete_post(context):
    context.app.profile_page.delete_post()


@then('Verify that the message {message_deleted} is displayed')
def verify_message_deleted(context, message_deleted):
    context.app.profile_page.verify_message_deleted(message_deleted)