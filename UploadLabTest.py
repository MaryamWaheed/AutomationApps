import os
import time
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

    # Enter the verification code
    for i, num in enumerate('1234'):
        verification_code_field = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("textInput").instance({i})'))
        )
        verification_code_field.send_keys(num)


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

    time.sleep(5)

    # Perform scroll using UiScrollable
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Medications"));')

    # Click on Medications
    medications_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Medications")'))
    )
    medications_button.click()

    # Click on Add New Medication button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add new medication")'))
    )
    add_button.click()

    # Locate the file input field and upload the image
    file_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Uplaod file/image")')))
    file_input.click()

    # Wait for the file chooser dialog to open
    # If it's a standard file input dialog, send the file path directly
    file_path = os.path.join(os.path.expanduser("~"), "Documents", "Image.jpg")
    file_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR,'new UiSelector().resourceId("com.google.android.documentsui:id/icon_mime_lg").instance(0)')))
    file_input.click()

    # Click on Type of medications
    type_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Choose").instance(0)'))
    )
    type_button.click()

    # Select first option
    select_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Medication_name")'))
    )
    select_button.click()

    # Click on Specific Type of medications
    type_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Choose").instance(1)'))
    )
    type_button.click()

    # Select first option
    select_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Medication_name")'))
    )
    select_button.click()

    # Click on Specific Type of medications
    type_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Choose").instance(2)'))
    )
    type_button.click()

    # Select first option
    select_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("200")'))
    )
    select_button.click()

    # Click on Add Medication button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add Medication")'))
    )
    add_button.click()

    # Back Button
    back_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'))
    )
    back_button.click()

    # Back Button
    back_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'))
    )
    back_button.click()

    # Perform scroll using UiScrollable
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Lab Tests"));')

    # Click on Lab Test
    lab_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Lab Tests")'))
    )
    lab_button.click()

    # Click on Add Lab Test button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add new lab test")'))
    )
    add_button.click()

    # Click on Add Lab Test button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Choose test name")'))
    )
    add_button.click()

    # Select Hemoglobin A1C test option
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Hemoglobin A1C test")'))
    )
    add_button.click()


    # Locate the file input field and upload the image
    file_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Uplaod file/image")')))
    file_input.click()

    # Wait for the file chooser dialog to open
    # If it's a standard file input dialog, send the file path directly
    file_path = os.path.join(os.path.expanduser("~"), "Documents", "Image.jpg")
    file_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.google.android.documentsui:id/icon_mime_lg").instance(0)'))
    )
    file_input.click()

    # Write result
    result_field = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Write Result")'))
    )
    result_field.send_keys('Yes,Thankyou.')

    # Click on Add Lab Test button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add lab test")'))
    )
    add_button.click()

    # Back Button
    back_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'))
    )
    back_button.click()

    # Perform scroll using UiScrollable
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
                        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Medical History"));')

    # Click on Medical History
    lab_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Medical History")'))
    )
    lab_button.click()

    # Click on Diagnosis Add new
    new_add = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add new").instance(0)'))
    )
    new_add.click()

    # Add new diagnosis
    add_new = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Please write diagnosis name")'))
    )
    add_new.send_keys('Zinc')

    # Click on Add diagnosis button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add diagnosis")'))
    )
    add_button.click()

    # Click on surgery Add new
    new_add = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add new").instance(1)'))
    )
    new_add.click()

    # Add new surgery
    add_new = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Please write surgery name")'))
    )
    add_new.send_keys('Zinc')

    # Click on Add surgery button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add surgery")'))
    )
    add_button.click()

    # Click on allergy Add new
    new_add = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add new").instance(2)'))
    )
    new_add.click()

    # Add new allergy
    add_new = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Please write allergy name")'))
    )
    add_new.send_keys('Zinc')

    # Click on Add allergy button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add allergy")'))
    )
    add_button.click()

    # Click on sensitivity Add new
    new_add = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add new").instance(3)'))
    )
    new_add.click()

    # Add new sensitivity
    add_new = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Please write med sensitivity ")'))
    )
    add_new.send_keys('Zinc')

    # Click on Add sensitivity button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Add sensitivity")'))
    )
    add_button.click()

    # Click on Save info button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Save Info")'))
    )
    add_button.click()

    # Back Button
    back_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(0)'))
    )
    back_button.click()

    # Perform scroll using UiScrollable
    driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("Body Activity Level"));')

    # Click on Body Activity Level
    lab_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Body Activity Level")'))
    )
    lab_button.click()

    # Click on first option
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Lethargic (No exercise per week)")'))
    )
    add_button.click()

    # Click on Save info button
    add_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Save Info")'))
    )
    add_button.click()

    # Back Button
    back_button = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable(
            (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView")'))
    )
    back_button.click()



finally:
    # pass
    pass
