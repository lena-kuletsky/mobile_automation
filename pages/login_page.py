from appium.webdriver.common.appiumby import AppiumBy

from pages.base_page import Page

from time import sleep


class LoginPage(Page):

    ALLOW = (AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button')
    GET_STARTED_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="Get Started"]')
    PHONE_FIELD = (AppiumBy.XPATH, '//android.widget.EditText')
    NEXT_BTN = (AppiumBy.XPATH, '//android.view.View[@content-desc="Next"]')

    def login(self):
        self.click(*self.ALLOW)
        self.click(*self.GET_STARTED_BTN)
        self.click(*self.PHONE_FIELD)
        self.input('2199234500', *self.PHONE_FIELD)
        self.click(*self.NEXT_BTN)
        sleep(8)
        self.input('111111', *self.PHONE_FIELD)
        self.click(*self.NEXT_BTN)


