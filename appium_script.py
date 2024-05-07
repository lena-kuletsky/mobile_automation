from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

from time import sleep


# desired_capabilities = {
#     "platformName": "Android",
#     "automationName": 'uiautomator2',
#     "platformVersion": "13",
#     "deviceName": "emulator-5554",
#     "appActivity": "com.hotake.hotake.MainActivity",
#     "appPackage": "com.stunt.dev.application",
#     "app": r"C:\Users\elena.kuletsky\Desktop\mobile_automation\mobile_app\app-dev-release.apk"
# }

desired_capabilities = {
    "platformName": "Android",
    "automationName": 'uiautomator2',
    "platformVersion": "13",
    "deviceName": "Pixel 8 Pro",
    "appActivity": "com.hotake.hotake.MainActivity",
    "appPackage": "com.stunt.dev.application",
    "app": r"C:\Users\elena.kuletsky\Desktop\mobile_automation\mobile_app\app-dev-release.apk"
}

appium_server_url = 'http://localhost:4723'
capabilities_options = UiAutomator2Options().load_capabilities(desired_capabilities)

driver = webdriver.Remote(appium_server_url, options=capabilities_options)
driver.implicitly_wait(5)

# Click Permission btn
driver.find_element(AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button').click()
# Click Get Started
driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Get Started"]').click()

#
# Click Search icon
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').click()
#
# Populate search field:
sleep(10)
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys('3865383918')

# click next
driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Next"]').click()


#
# # Verification
# expected_result = 'Python (programming language)'
# actual_result = driver.find_element(AppiumBy.ID, 'org.wikipedia:id/page_list_item_title').text
#
# assert actual_result == expected_result, f'Expected {expected_result} did not match actual {actual_result}'
#
# driver.quit()