import time
import logging
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def set_up_appium() -> object:
    """Set up the Appium driver with desired capabilities."""
    options = AppiumOptions()
    options.set_capability('platformName', 'android')
    options.set_capability('platformVersion', '11')
    options.set_capability('deviceName', 'RZ8M61HGKEK')
    options.set_capability('automationName', 'UiAutomator2')
    options.set_capability('appPackage', 'com.ithnain.ithnainapp')
    options.set_capability('appActivity', 'com.ithnain.ithnainapp.MainActivity')
    options.set_capability('uiautomator2ServerLaunchTimeout', 60000)

    return webdriver.Remote("http://127.0.0.1:4723", options=options)


def wait_and_click(driver, locator, timeout=20):
    """Wait for an element to be clickable and then click it."""
    try:
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        element.click()
        logging.info(f"Clicked on element: {locator}")
    except Exception as e:
        logging.error(f"Failed to click on element: {locator}, Error: {e}")
        raise


def wait_and_send_keys(driver, locator, text, timeout=20):
    """Wait for an element to be present and then send keys to it."""
    try:
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        element.send_keys(text)
        logging.info(f"Sent keys to element: {locator}")
    except Exception as e:
        logging.error(f"Failed to send keys to element: {locator}, Error: {e}")
        raise


def set_picker_value(driver, picker_locator, value):
    """Set the value of a NumberPicker directly."""
    try:
        picker = WebDriverWait(driver, 20).until(EC.presence_of_element_located(picker_locator))
        picker.clear()
        picker.send_keys(value)
        logging.info(f"Set picker value to: {value}")
    except Exception as e:
        logging.error(f"Failed to set picker value: {value} in picker: {picker_locator}, Error: {e}")
        raise


def select_full_date(driver):
    """Select the date by setting date, month, and year, and then clicking OK."""
    date_picker = (By.XPATH, '//android.widget.NumberPicker[1]//android.widget.EditText')
    month_picker = (By.XPATH, '//android.widget.NumberPicker[2]//android.widget.EditText')
    year_picker = (By.XPATH, '//android.widget.NumberPicker[3]//android.widget.EditText')
    OK_BUTTON = (By.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')

    logging.info("Setting Day...")
    set_picker_value(driver, date_picker, "3")
    logging.info("Day Set!")
    time.sleep(1)

    logging.info("Setting Month...")
    set_picker_value(driver, month_picker, "Jul")
    logging.info("Month Set!")
    time.sleep(1)

    logging.info("Setting Year...")
    set_picker_value(driver, year_picker, "2021")
    logging.info("Year Set!")
    time.sleep(1)

    wait_and_click(driver, OK_BUTTON)
    logging.info("Date Selection Confirmed!")


def retrieve_otp_from_whatsapp(driver):
    """Switch to WhatsApp, retrieve OTP, and return to the main app."""
    try:
        # Switch to WhatsApp
        driver.activate_app("com.whatsapp")
        time.sleep(5)  # Wait for WhatsApp to load

        # Locate the latest OTP message by text
        otp_message_locator = (By.XPATH, '//android.widget.TextView[contains(@text, "Ithnainofficial")]')
        otp_message_elements = driver.find_elements(*otp_message_locator)


        print(otp_message_locator)
        print(otp_message_elements)

        if not otp_message_elements:
            raise Exception("No OTP messages found")

        # Get the last message (assumed to be the latest)
        latest_otp_message_element = otp_message_elements[-1]
        # Extract OTP from the message
        otp = latest_otp_message_element.text

        print(latest_otp_message_element)

        # If you want to directly copy, ensure you click the 'Copy code' button
        copy_button_locator = (By.XPATH, '//android.widget.TextView[contains(@text, "Copy code")]')
        try:
            copy_button = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(copy_button_locator))
            copy_button.click()
            logging.info("Code Copied")
        except Exception as e:
            logging.error(f"Copy code button not found: {e}")
            raise

        # Switch back to the main app
        driver.activate_app("com.ithnain.ithnainapp")
        return otp
    except Exception as e:
        logging.error(f"Failed to retrieve OTP, Error: {e}")
        raise


def main():
    driver = set_up_appium()
    driver.implicitly_wait(10)

    try:
        # Constants for element locators
        LANG_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')
        LOGIN_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
        TEXT_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("🇸🇦")')
        COUNTRY_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("text-input-country-filter")')
        PAK_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pakistan (+92)")')
        PHONE_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone number")')
        LOGIN1_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
        VERIFICATION_CODE_FIELD = lambda fn: (By.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("textInput").instance({fn})')
        OTHER_PATIENTS = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("other patients.")')
        NEXT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
        I_AM_PATIENT = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("I am the patient")')
        PATIENT_NAME = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Write patient name.")')
        MALE_GENDER = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Male")')
        NEXT2_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(2)')
        DIABETES_TYPE1 = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Type 1 diabetes")')
        EDIT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Edit")')
        EDIT1_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Edit")')
        CHECKBOX = lambda fn: (By.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("RNE__Checkbox__Icon").instance({fn})')
        GOAL_SELECT = lambda text, fn: (By.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}").instance({fn})')
        SUBMIT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("submit")')
        NOT_NOW = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NOT NOW")')

        # Click on Language Button
        wait_and_click(driver, LANG_BUTTON)

        # Click on Login Button
        wait_and_click(driver, LOGIN_BUTTON)

        # Click on Text Field
        wait_and_click(driver, TEXT_FIELD)

        # Send keys to Country Field and select Pakistan
        wait_and_send_keys(driver, COUNTRY_FIELD, 'Pakistan')
        wait_and_click(driver, PAK_FIELD)

        # Send keys to Phone Number Field
        wait_and_send_keys(driver, PHONE_FIELD, '3091431565')

        # Click on Login Button
        wait_and_click(driver, LOGIN1_BUTTON)

        # Retrieve and enter the verification code from WhatsApp
        otp = retrieve_otp_from_whatsapp(driver)

        # Enter the OTP into the verification code fields
        for idx, digit in enumerate(otp):
            wait_and_send_keys(driver, VERIFICATION_CODE_FIELD(idx), digit)

        # Click on Medical Referral
        wait_and_click(driver, OTHER_PATIENTS)

        # Click on Next Button
        wait_and_click(driver, NEXT_BUTTON)

        # Select "I am the patient" option
        wait_and_click(driver, I_AM_PATIENT)

        # Send keys to Patient Name
        wait_and_send_keys(driver, PATIENT_NAME, 'AHMAD')

        # Select Male Gender
        wait_and_click(driver, MALE_GENDER)

        # Click on Next Button again
        wait_and_click(driver, NEXT2_BUTTON)

        # Select Type 1 Diabetes
        wait_and_click(driver, DIABETES_TYPE1)

        # Click on Next Button again
        wait_and_click(driver, NEXT2_BUTTON)

        # Click on Edit Button
        wait_and_click(driver, EDIT_BUTTON)

        # Select the date again
        select_full_date(driver)

        # Click on Next Button again
        wait_and_click(driver, NEXT2_BUTTON)

        # Click on Edit Button
        wait_and_click(driver, EDIT1_BUTTON)

        # Select the date again
        select_full_date(driver)

        # Click on Next Button again
        wait_and_click(driver, NEXT2_BUTTON)

        # Check checkboxes
        for idx in range(3):
            wait_and_click(driver, CHECKBOX(idx))

        # Click on Next Button
        wait_and_click(driver, NEXT2_BUTTON)

        # Select Goal
        goals = [("Carb Counting", 0), ("Weight Loss", 0), ("Reduce Diabetes", 0)]
        for goal_text, instance_idx in goals:
            wait_and_click(driver, GOAL_SELECT(goal_text, instance_idx))

        # Click on others button and send keys
        wait_and_click(driver, GOAL_SELECT("Others", 0))
        wait_and_send_keys(driver, GOAL_SELECT("Write your goal", 0), 'Major Goal')

        # Click on submit button
        wait_and_click(driver, SUBMIT_BUTTON)

        # Click on Not Now button
        wait_and_click(driver, NOT_NOW)

    finally:
        # Pass the driver
        pass


if __name__ == "__main__":
    main()
