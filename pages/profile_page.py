from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page

from time import sleep


class ProfilePage(Page):

    MY_PROFILE_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="My Profile"]')
    TAKES_TAB = (AppiumBy.XPATH, '//android.view.View[@content-desc="Takes"]')
    POST_TAKE = (AppiumBy.XPATH, '//android.view.View[@content-desc="Sarah Fan @sarahfan 23m I love sport"]')
    THREE_DOT_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="Thread"]/android.view.View[2]/android.view.View[6]')
    DELETE_OPTION = (AppiumBy.XPATH, '//android.view.View[@content-desc="Option Delete this post"]')
    MESSAGE_DELETED = (AppiumBy.XPATH, '//android.view.View[@content-desc="Your post has been deleted"]')

    def tap_my_profile(self):
        sleep(5)
        self.click(*self.MY_PROFILE_BTN)

    def tap_takes_tab(self):
        self.click(*self.TAKES_TAB)

    def select_post(self):
        sleep(7)
        self.click(*self.POST_TAKE)

    def tap_three_dot_button(self):
        sleep(2)
        self.click(*self.THREE_DOT_BTN)

    def delete_post(self):
        self.click(*self.DELETE_OPTION)

    def verify_message_deleted(self, message_deleted):
        self.verify_text(message_deleted, *self.MESSAGE_DELETED)
