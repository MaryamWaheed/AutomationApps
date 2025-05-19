from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

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
        EC.element_to_be_clickable((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")'))
    )
    lang_button.click()

    # Wait for the login button to be clickable and click it
    login_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Create new account")'))
    )
    login_button.click()

    # Wait for the text field to be present and find it
    text_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("🇸🇦")'))
    )
    text_field.click()

    # Wait for the country input field to be present and find it
    country_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("text-input-country-filter")'))
    )
    country_field.send_keys('Pakistan')

    # Wait for the Pakistan country to be present and click it
    pak_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pakistan (+92)")'))
    )
    pak_field.click()

    # Wait for the phone number input field to be present and find it
    phone_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone Number")'))
    )
    phone_field.send_keys('3068805991')

    # Check Terms and Conditions
    pak_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("RNE__ICON__Component")'))
    )
    pak_field.click()

    # Click on signup button
    signup_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Signup")'))
    )
    signup_button.click()

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

    # # Click on None (I don't have a referral)
    # screen_button = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("None (I dont have a referral).")'))
    # )
    # screen_button.click()

    # Click on a Through a medical referral
    screen_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Through a medical referral.")'))
    )
    screen_button.click()

    # Type your medical referral code
    screen_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Type your medical referral code.")'))
    )
    screen_button.send_keys('Yes')

    # Select other patients option
    screen_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("other patients.")'))
    )
    screen_button.click()

    # Select other option
    screen_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Other.")'))
    )
    screen_button.click()

    # Type other option
    screen_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Type other option.")'))
    )
    screen_button.send_keys('Yes')

    # Next
    screen_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'))
    )
    screen_button.click()


finally:
    # pass
    pass
