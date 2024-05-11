from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import Page

from time import sleep


class MainPage(Page):

    PLUS_BTN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[9]')
    POST_TAKE_OPTION = (AppiumBy.XPATH, '//android.view.View[@content-desc="Post a Take"]')
    FIELD_TEXT = (AppiumBy.XPATH, '//android.widget.EditText')
    POST_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="Post"]')
    FOLLOWING_TAB = (AppiumBy.XPATH, '//android.view.View[@content-desc="Following"]')

    SEARCH_ICON = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[3]')
    SEARCH_FIELD = (AppiumBy.XPATH, '//android.widget.EditText')
    PEOPLE_TAB = (AppiumBy.XPATH, '//android.view.View[@content-desc="People"]')
    ACCOUNT = (AppiumBy.XPATH, '//android.view.View[@content-desc="@Hammes_Nicklaus"]')
    FOLLOW_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="Following"]')
    BACK_BTN = (AppiumBy.XPATH, '//android.widget.FrameLayout[@resource-id="android:id/content"]/android.widget.FrameLayout/android.view.View/android.view.View/android.view.View/android.view.View/android.view.View[1]')
    CANCEL_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="Cancel"]')
    FOLLOWING = (AppiumBy.XPATH, '//android.view.View[@content-desc="8 Following"]')

# Create Post test

    def tap_plus_btn(self):
        sleep(10)
        self.click(*self.PLUS_BTN)
        # self.wait_for_element_appear(*self.PLUS_BTN)
        # self.wait_for_element_click(*self.PLUS_BTN)

    def tap_post_take(self):
        self.wait_for_element_click(*self.POST_TAKE_OPTION)

    def enter_text(self, input_text):
        self.wait_for_element_appear(*self.FIELD_TEXT)
        self.input(input_text, *self.FIELD_TEXT)

    def publish_post(self):
        self.wait_for_element_click(*self.POST_BTN)

    def verify_published_post(self):
        wait = WebDriverWait(self.driver, 70)
        wait.until(EC.presence_of_element_located(self.FOLLOWING_TAB))
        self.find_element(*self.FOLLOWING_TAB)
        # self.wait_for_element_appear(*self.PUBLISHED_POST)

# Follow test

    def tap_search_icon(self):
        self.wait_for_element_appear(*self.SEARCH_ICON)
        self.wait_for_element_click(*self.SEARCH_ICON)

    def enter_text_search_field(self, text):
        sleep(5)
        self.input(text, *self.SEARCH_ICON)

    def tap_people_tab(self):
        self.wait_for_element_click(*self.PEOPLE_TAB)

    def pick_account_from_list(self):
        self.wait_for_element_appear(*self.ACCOUNT)
        self.wait_for_element_click(*self.ACCOUNT)

    def tap_follow_button(self):
        self.wait_for_element_appear(*self.FOLLOW_BTN)
        self.wait_for_element_click(*self.FOLLOW_BTN)

    def tap_back_button(self):
        self.wait_for_element_click(*self.BACK_BTN)

    def tap_cancel_button(self):
        self.wait_for_element_click(*self.CANCEL_BTN)

    def tap_following(self):
        self.wait_for_element_click(*self.FOLLOWING)

    def verify_list_following(self):
        self.wait_for_element_appear(*self.ACCOUNT)

# Spark creation test

