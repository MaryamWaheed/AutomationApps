import time
import random
import logging
from appium import webdriver
from appium.options.common import AppiumOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def set_up_appium():
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


def wait_and_click(driver, locator, timeout=50):
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
    """Select the date by scrolling and setting a random day, month, and year, and then clicking OK."""
    # Locators for day, month, and year pickers
    date_picker = (By.XPATH, '//android.widget.NumberPicker[1]//android.widget.EditText')
    month_picker = (By.XPATH, '//android.widget.NumberPicker[2]//android.widget.EditText')
    year_picker = (By.XPATH, '//android.widget.NumberPicker[3]//android.widget.EditText')
    OK_BUTTON = (By.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')

    # Generate random day, month, and year
    random_day = str(random.randint(1, 30))  # You can adjust this depending on the month's actual day range
    random_month = random.choice(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    random_year = str(random.randint(1990, 2023))  # Adjust year range as needed

    # Scroll to and select the day
    logging.info(f"Setting Day: {random_day}")
    set_picker_value(driver, date_picker, random_day)
    print(f"Day Set: {random_day}")
    time.sleep(2)

    # Scroll to and select the month
    logging.info(f"Setting Month: {random_month}")
    set_picker_value(driver, month_picker, random_month)
    print(f"Month Set: {random_month}")
    time.sleep(2)

    # Scroll to and select the year
    logging.info(f"Setting Year: {random_year}")
    set_picker_value(driver, year_picker, random_year)
    print(f"Year Set: {random_year}")
    time.sleep(2)

    # Click OK button to confirm the selection
    wait_and_click(driver, OK_BUTTON)
    print("Date Selection Confirmed!")
    time.sleep(3)


def retrieve_otp_from_whatsapp(driver):

        try:
            # Switch to WhatsApp
            driver.activate_app("com.whatsapp")
            time.sleep(15)  # Wait for WhatsApp to load

            print("Searching for the chat")

            # Locate the chat by name and click to open it
            chat_locator = (By.XPATH, '//android.widget.TextView[@text="Ithnainofficial"]')
            chat_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(chat_locator))
            chat_element.click()
            print("Chat opened")

            time.sleep(10)  # Wait for chat to load

            # Locate the latest OTP message in the chat
            print("Locating the latest OTP message...")
            otp_message_locator = (By.XPATH, '//android.widget.TextView[contains(@text, "is your verification code")]')
            otp_message_elements = driver.find_elements(*otp_message_locator)

            if not otp_message_elements:
                print("No OTP messages found in the chat")
                raise Exception("No OTP messages found in the chat")

            # Get the last message (assumed to be the latest)
            latest_otp_message_element = otp_message_elements[-1]

            # Extract the OTP from the latest message
            otp_text = latest_otp_message_element.get_attribute('text')
            logging.info(f"Full OTP Message Text: {otp_text}")

            otp = ''.join(filter(str.isdigit, otp_text))  # Extract digits as the OTP
            logging.info(f"Extracted OTP: {otp}")

            if not otp:
                logging.error("No OTP found in the message text")
                raise Exception("No OTP found in the message text")

            print(f"Retrieved OTP: {otp}")

            print("otp",otp)

            driver.set_clipboard_text(otp)

            # Switch back to the main app
            print("Switching back to the main app...")
            driver.activate_app("com.ithnain.ithnainapp")
            return otp
        except Exception as e:
            logging.error(f"Failed to retrieve OTP, Error: {e}")
            raise


def main():
    driver = set_up_appium()
    driver.implicitly_wait(50)

    try:
        # # Constants for element locators
        time.sleep(70)
        LANG_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')
        SIGNUP_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Create new account")')
        TEXT_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("🇸🇦")')
        COUNTRY_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter country name")')
        PAK_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pakistan (+92)")')
        PHONE_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone number")')
        TERMS_CHECKBOX = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("RNE__ICON__Component")')
        SIGNUP1_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("android.view.ViewGroup").instance(29)')
        AGREE_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Agree")')
        OTHER_PATIENTS = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Other patients.")')
        NEXT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
        I_AM_PATIENT = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("I am the patient")')
        PATIENT_NAME = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Write patient name.")')
        MALE_GENDER = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Male")')
        NEXT2_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(2)')
        DIABETES_TYPE1 = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Type 1 diabetes")')
        EDIT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Edit")')
        EDIT1_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Edit")')
        CHECKBOX = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("RNE__ICON__Component").instance(0)')
        CHECKBOX1 = lambda fn: (By.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("RNE__Checkbox__Icon").instance({fn})')
        GOAL_SELECT = lambda text, fn: (By.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}").instance({fn})')
        SUBMIT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Submit")')
        NOT_NOW = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Not Now")')

        # Click on Language Button
        wait_and_click(driver, LANG_BUTTON)

        # Click on Login Button
        wait_and_click(driver, SIGNUP_BUTTON)

        # Click on Text Field
        wait_and_click(driver, TEXT_FIELD)

        # Send keys to Country Field and select Pakistan
        wait_and_send_keys(driver, COUNTRY_FIELD, 'Pakistan')
        wait_and_click(driver, PAK_FIELD)

        # Send keys to Phone Number Field
        wait_and_send_keys(driver, PHONE_FIELD, '3091431565')

        # Check Terms and Conditions
        wait_and_click(driver, TERMS_CHECKBOX)

        # Click on Login Button
        wait_and_click(driver, SIGNUP1_BUTTON)

        # Retrieve and enter the verification code from WhatsApp
        retrieve_otp_from_whatsapp(driver)

        # Click on Agree Button
        wait_and_click(driver, AGREE_BUTTON)

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

        # Click on Next Button again
        wait_and_click(driver, CHECKBOX)

        # Check checkboxes
        for idx in range(3):
            wait_and_click(driver, CHECKBOX1(idx))

        # Click on Next Button
        wait_and_click(driver, NEXT2_BUTTON)

        # Select Goal
        goals = [("Carb Counting", 0), ("Weight Loss", 0), ("Reduce Diabetes", 0)]
        for goal_text, instance_idx in goals:
            wait_and_click(driver, GOAL_SELECT(goal_text, instance_idx))


        # Click on submit button
        wait_and_click(driver, SUBMIT_BUTTON)

        # Click on Not Now button
        wait_and_click(driver, NOT_NOW)

    finally:
        # Pass the driver
        pass


if __name__ == "__main__":
    main()
