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

    def tap_plus_btn(self):
        sleep(5)
        self.click(*self.PLUS_BTN)

    def tap_post_take(self):
        sleep(2)
        self.click(*self.POST_TAKE_OPTION)

    def enter_text(self, input_text):
        sleep(2)
        self.input(input_text, *self.FIELD_TEXT)

    def publish_post(self):
        self.click(*self.POST_BTN)

    def verify_published_post(self):
        wait = WebDriverWait(self.driver, 70)
        wait.until(EC.presence_of_element_located(self.FOLLOWING_TAB))
        self.find_element(*self.FOLLOWING_TAB)
        # self.wait_for_element_appear(*self.PUBLISHED_POST)

