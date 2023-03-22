import time

from appium import webdriver

des_cap = {
    "platformName": "android",
    "deviceName": "oneplus",
    "app": r"C:\paras_shah\python_scripts\appium_project\khan-academy-7-3-2.apk",
    "udid": "emulator-5554"
}

driver = webdriver.Remote(command_executor="http://127.0.0.1:4723/wd/hub", desired_capabilities=des_cap)

print(driver.page_source)

time.sleep(5)

driver.quit()

