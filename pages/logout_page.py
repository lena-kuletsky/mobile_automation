from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page

from time import sleep


class LogoutPage(Page):

    AVATAR = (AppiumBy.XPATH, '//android.view.View[./android.view.View[@content-desc="Scheduled"]]/android.view.View[@index="2"]')
    SETTINGS = (AppiumBy.XPATH, '//android.view.View[@content-desc="Settings"]')
    LOGOUT_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="Logout"]')
    YES_BTN = (AppiumBy.XPATH, '//android.widget.Button[@content-desc="Yes"]')
    SETTINGS_HEADER = (AppiumBy.XPATH, '//android.view.View[@content-desc="Settings"]')

    def tap_avatar(self):
        sleep(8)
        self.wait_for_element_click(*self.AVATAR)

    def tap_settings(self):
        self.wait_for_element_appear(*self.SETTINGS)
        sleep(3)
        self.wait_for_element_click(*self.SETTINGS)

    def tap_logout(self):
        self.wait_for_element_appear(*self.LOGOUT_BTN)
        self.click_by_element_coordinates(50, 98, *self.LOGOUT_BTN)

    def tap_yes_btn(self):
        self.wait_for_element_click(*self.YES_BTN)

    def verify_logout(self):
        self.wait_for_element_disappear(*self.SETTINGS_HEADER)