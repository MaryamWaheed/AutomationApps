from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Appium options
options = AppiumOptions()
options.set_capability('platformName', 'android')
options.set_capability('platformVersion', '11')
options.set_capability('deviceName', 'RZ8M61HGKEK')
options.set_capability('automationName', 'UiAutomator2')
options.set_capability('appPackage', 'com.tepia.moodme')
options.set_capability('appActivity', 'com.tepia.moodme.MainActivity')

# Initialize Appium driver
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
driver.implicitly_wait(10)

try:
    # Wait for the login button to be clickable and click it
    signup_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Sign Up")'))
    )
    signup_button.click()

finally:
    # pass
    pass
