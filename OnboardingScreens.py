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
    phone_field.send_keys('3064380090')

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

    # Enter the verification code
    for i, num in enumerate('1234'):
        verification_code_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located(
                (By.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("textInput").instance({i})'))
        )
        verification_code_field.send_keys(num)

    # # Click on None (I don't have a referral)
    # screen_button = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located(
    #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("None (I dont have a referral).")'))
    # )
    # screen_button.click()

    # Click on a Through a medical referral
    screen_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Through a medical referral.")'))
    )
    screen_button.click()

    # Type your medical referral code
    screen_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Type your medical referral code.")'))
    )
    screen_button.send_keys('Yes')

    # # Select other patients option
    # screen_button = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located(
    #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("other patients.")'))
    # )
    # screen_button.click()

    # # Select other option
    # screen_button = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located(
    #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Other.")'))
    # )
    # screen_button.click()
    #
    # # Type other option
    # screen_button = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located(
    #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Type other option.")'))
    # )
    # screen_button.send_keys('Yes')

    # Next
    screen_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)'))
    )
    screen_button.click()

    # Select I am the patient option
    screen2_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("I am the patient")'))
    )
    screen2_button.click()

    # write patient name
    pname_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Write patient name.")'))
    )
    pname_field.send_keys('Laila')

    # select female gender
    gender_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Female")'))
    )
    gender_button.click()

    # # select male gender
    # gender_button = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located(
    #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Male")'))
    # )
    # gender_button.click()

    # Select One of my parents option
    screen2_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("One of my parents")'))
    )
    screen2_button.click()

    # write your  name
    pname_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Write your name")'))
    )
    pname_field.send_keys('Ambani')

    # write patient name
    pname_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Write patient name")'))
    )
    pname_field.send_keys('Anant')
    #
    # # select female gender
    # gender_button = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located(
    #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Female")'))
    # )
    # gender_button.click()
    #
    # # # select male gender
    # # gender_button = WebDriverWait(driver, 20).until(
    # #     EC.presence_of_element_located(
    # #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Male")'))
    # # )
    # # gender_button.click()
    #
    # Select One of my kids option
    screen2_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("One of my kids")'))
    )
    screen2_button.click()

    # write your  name
    pname_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Write your name")'))
    )
    pname_field.send_keys('Ambani')

    # write patient name
    pname_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Write patient name")'))
    )
    pname_field.send_keys('Anant')

    # select female gender
    gender_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Female")'))
    )
    gender_button.click()

    # # # select male gender
    # # gender_button = WebDriverWait(driver, 20).until(
    # #     EC.presence_of_element_located(
    # #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Male")'))
    # # )
    # # gender_button.click()
    #
    # # Select Other option
    # screen2_button = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located(
    #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Other")'))
    # )
    # screen2_button.click()
    #
    # # Select Other option
    # screen2_button = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located(
    #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Choose who is patient")'))
    # )
    # screen2_button.click()
    #
    # # # Select In-laws relatives (daughter-in-law/son-in-law) option
    # # screen2_button = WebDriverWait(driver, 20).until(
    # #     EC.presence_of_element_located(
    # #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("new UiSelector().text("In-laws relatives (daughter-in-law/son-in-law)")")'))
    # # )
    # # screen2_button.click()
    # #
    # # # Select Friend option
    # # screen2_button = WebDriverWait(driver, 20).until(
    # #     EC.presence_of_element_located(
    # #         (By.ANDROID_UIAUTOMATOR,
    # #          'new UiSelector().text("new UiSelector().text("Friend")'))
    # # )
    # # screen2_button.click()
    #
    # # Touch Action
    # actions = ActionChains(driver)
    # actions.w3c_actions = ActionBuilder(driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
    # actions.w3c_actions.pointer_action.move_to_location(533, 1631)
    # actions.w3c_actions.pointer_action.pointer_down()
    # actions.w3c_actions.pointer_action.move_to_location(546, 885)
    # actions.w3c_actions.pointer_action.release()
    # actions.perform()
    #
    # # Select Second-degree relatives (uncle/aunt) option
    # screen2_button = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located(
    #         (By.ANDROID_UIAUTOMATOR,'new UiSelector().text("Second-degree relatives (uncle/aunt)")'))
    # )
    # screen2_button.click()
    #
    # # Write Your Name
    # pname_field = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Write your name")'))
    # )
    # pname_field.send_keys('Ambani')
    #
    # # write patient name
    # pname_field = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Write patient name")'))
    # )
    # pname_field.send_keys('Anant')
    #
    # # select female gender
    # gender_button = WebDriverWait(driver, 20).until(
    #     EC.presence_of_element_located(
    #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Female")'))
    # )
    # gender_button.click()
    #
    # # # select male gender
    # # gender_button = WebDriverWait(driver, 20).until(
    # #     EC.presence_of_element_located(
    # #         (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Male")'))
    # # )
    # # gender_button.click()

    # Next
    screen_button = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(2)'))
    )
    screen_button.click()

finally:
    # pass
    pass
