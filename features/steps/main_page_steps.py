from behave import given, when, then


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
