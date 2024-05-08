from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from appium.options.android import UiAutomator2Options

from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from time import sleep

desired_capabilities = {
    "platformName": "Android",
    "automationName": 'uiautomator2',
    "platformVersion": "13",
    "deviceName": "emulator-5554",
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
# Click phone field:
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').click()
#
# Populate phone:
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys('2199234500')

# click next
driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Next"]').click()

# click verification field
sleep(7)
driver.find_element(AppiumBy.XPATH, '//android.widget.EditText').send_keys('111111')

# click next
driver.find_element(AppiumBy.XPATH, '//android.view.View[@content-desc="Next"]').click()
#
# Verification
driver.find_element(AppiumBy.XPATH, '(//android.view.View[@content-desc="Sparks"])[2]')




# Verification
# expected_result = 'Python (programming language)'
# actual_result = driver.find_element(AppiumBy.ID, 'org.wikipedia:id/page_list_item_title').text
#
# assert actual_result == expected_result, f'Expected {expected_result} did not match actual {actual_result}'
#
