from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set up Appium options
options = AppiumOptions()
options.set_capability('platformName', 'android')
options.set_capability('platformVersion', '11')
options.set_capability('deviceName', 'RZ8M61HGKEK')
options.set_capability('automationName', 'UiAutomator2')
options.set_capability('appPackage', 'com.ithnain_patient_app')
options.set_capability('appActivity', 'com.ithnain_patient_app.MainActivity')
options.set_capability('uiautomator2ServerLaunchTimeout', 60000)

# Initialize Appium driver
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)
driver.implicitly_wait(10)

try:
    # Wait for the language button to be clickable and click it
    lang_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")'))
    )
    lang_button.click()

    # Wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")'))
    )
    login_button.click()

    # Wait for the text field to be present and find it
    text_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("🇸🇦")'))
    )
    text_field.click()

    # Wait for the country input field to be present and find it
    country_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("text-input-country-filter")'))
    )
    country_field.send_keys('Pakistan')

    # Wait for the Pakistan country to be present and click it
    pak_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pakistan (+92)")'))
    )
    pak_field.click()

    # Wait for the phone number input field to be present and find it
    phone_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone Number")'))
    )
    phone_field.send_keys('3068804884')

    # Wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")'))
    )
    login_button.click()

    # Wait for the verification code input field to be present and find it
    verification_code_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("textInput").instance(0)'))
    )
    verification_code_field.send_keys('1')
    # Wait for the verification code input field to be present and find it
    verification_code_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("textInput").instance(1)'))
    )
    verification_code_field.send_keys('2')
    # Wait for the verification code input field to be present and find it
    verification_code_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("textInput").instance(2)'))
    )
    verification_code_field.send_keys('3')
    # Wait for the verification code input field to be present and find it
    verification_code_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("textInput").instance(3)'))
    )
    verification_code_field.send_keys('4')

    # Click on Profile icon
    profile_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(72)'))
    )
    profile_button.click()

    # Perform scroll using UiScrollable
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Weight and Height"));')

    # Click on Weight and Height
    lab_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Weight and Height")'))
    )
    lab_button.click()

    # Debug print to confirm we reached this point
    print("Reached the height and weight fields")

    # Enter value in height field
    height_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("36")'))
    )
    height_field.clear()
    print("Entered value in height field.")

    # Enter value in height field
    height_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Height in ft")'))
    )
    height_field.send_keys('36')
    print("Entered value in height field.")

    # Enter value in weight field
    weight_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("9")'))
    )
    weight_field.clear()
    print("Cleared.")

    weight_field = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter Weight in kg")'))
    )
    weight_field.send_keys('9')
    print("Entered value in weight field.")

    # Debug print to confirm we entered the values
    print("Entered values in height and weight fields")

    # Click on Add Info button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add Info")'))
    )
    add_button.click()

finally:
    # pass
    pass
