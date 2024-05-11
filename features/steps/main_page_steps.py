from behave import given, when, then

# Post creation test


@when('Tap on Plus button at the bottom of the screen')
def tap_plus_btn(context):
    context.app.main_page.tap_plus_btn()


@when('Tap on /Post a Take/ from popup menu')
def tap_post_take(context):
    context.app.main_page.tap_post_take()


@when('Enter text {input_text} in the text field')
def enter_text(context, input_text):
    context.app.main_page.enter_text(input_text)


@when('Tap on ‘Post’ to publish')
def publish_post(context):
    context.app.main_page.publish_post()


@then('Verify that post was published')
def verify_published_post(context):
    context.app.main_page.verify_published_post()


# Follow test


@when('Tap on ‘search’ icon')
def tap_search_icon(context):
    context.app.main_page.tap_search_icon()


@when('Enter text {text} in the search field')
def enter_text_search_field(context, text):
    context.app.main_page.enter_text_search_field(text)


@when('Tap on ‘People’ tab under search field')
def tap_people_tab(context):
    context.app.main_page.tap_people_tab()


@when('Pick account from the list')
def pick_account_from_list(context):
    context.app.main_page.pick_account_from_list()


@when('Tap on ‘Follow’ button')
def tap_follow_button(context):
    context.app.main_page.tap_follow_button()


@when('Tap on Back button')
def tap_back_button(context):
    context.app.main_page.tap_back_button()


@when('Tap on Cancel button')
def tap_cancel_button(context):
    context.app.main_page.tap_cancel_button()


@when('Tap on Following in the My Profile page')
def tap_following(context):
    context.app.main_page.tap_following()


@then('Verify that following list reflects the addition')
def verify_list_following(context):
    assert context.app.main_page.verify_list_following()

