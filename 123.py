import time
import random
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


def wait_and_click(driver, locator, timeout=30):
    """Wait for an element to be clickable and then click it."""
    try:
        print(f"Waiting for element to be clickable: {locator}")
        element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
        print(f"Element found and clicked: {locator}")
        element.click()
    except Exception as e:
        print(f"Error: Failed to click on element {locator}, Error: {e}")
        raise


def wait_and_send_keys(driver, locator, text, timeout=30):
    """Wait for an element to be present and then send keys to it."""
    try:
        print(f"Waiting for element to send keys: {locator}")
        element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
        element.send_keys(text)
        print(f"Sent keys to element: {locator}, Text: {text}")
    except Exception as e:
        print(f"Error: Failed to send keys to element {locator}, Error: {e}")
        raise


def set_picker_value(driver, picker_locator, value):
    """Set the value of a NumberPicker directly."""
    try:
        print(f"Setting picker value: {value}")
        picker = WebDriverWait(driver, 20).until(EC.presence_of_element_located(picker_locator))
        picker.clear()
        picker.send_keys(value)
        print(f"Picker value set: {value}")
    except Exception as e:
        print(f"Error: Failed to set picker value: {value}, Error: {e}")
        raise


def select_full_date(driver):
    """Select the date by scrolling and setting a random day, month, and year, and then clicking OK."""
    date_picker = (By.XPATH, '//android.widget.NumberPicker[1]//android.widget.EditText')
    month_picker = (By.XPATH, '//android.widget.NumberPicker[2]//android.widget.EditText')
    year_picker = (By.XPATH, '//android.widget.NumberPicker[3]//android.widget.EditText')
    OK_BUTTON = (By.XPATH, '//android.widget.Button[@resource-id="android:id/button1"]')

    random_day = str(random.randint(1, 30))
    random_month = random.choice(["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"])
    random_year = str(random.randint(1990, 2023))

    print(f"Setting Day: {random_day}")
    set_picker_value(driver, date_picker, random_day)
    time.sleep(3)

    print(f"Setting Month: {random_month}")
    set_picker_value(driver, month_picker, random_month)
    time.sleep(3)

    print(f"Setting Year: {random_year}")
    set_picker_value(driver, year_picker, random_year)
    time.sleep(3)

    wait_and_click(driver, OK_BUTTON)
    print("Date Selection Confirmed!")
    time.sleep(5)  # Add a delay here

    # After confirming date selection
    time.sleep(3)  # Give some time for the UI to refresh
    DATE_DISPLAY = (By.XPATH, '//android.widget.TextView[@text="Newborn"]')  # Update this XPath

    try:
        date_display_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(DATE_DISPLAY))
        displayed_date = date_display_element.get_attribute('text')
        print(f"Displayed Date: {displayed_date}")
    except Exception as e:
        print(f"Error: Could not find displayed date, Error: {e}")


def retrieve_otp_from_whatsapp(driver):
    try:
        print("Switching to WhatsApp...")
        driver.activate_app("com.whatsapp")
        time.sleep(10)  # Wait for WhatsApp to load

        print("Searching for the chat 'Ithnainofficial'")
        chat_locator = (By.XPATH, '//android.widget.TextView[@text="Ithnainofficial"]')
        chat_element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable(chat_locator))
        chat_element.click()

        print("Locating the latest OTP message...")
        otp_message_locator = (By.XPATH, '//android.widget.TextView[contains(@text, "is your verification code")]')
        otp_message_elements = driver.find_elements(*otp_message_locator)

        if not otp_message_elements:
            print("No OTP messages found in the chat")
            raise Exception("No OTP messages found in the chat")

        latest_otp_message_element = otp_message_elements[-1]
        otp_text = latest_otp_message_element.get_attribute('text')
        print(f"Full OTP Message Text: {otp_text}")

        otp = ''.join(filter(str.isdigit, otp_text))
        if not otp:
            print("No OTP found in the message text")
            raise Exception("No OTP found in the message text")

        print(f"Retrieved OTP: {otp}")
        driver.set_clipboard_text(otp)

        print("Switching back to the main app...")
        driver.activate_app("com.ithnain.ithnainapp")
        return otp
    except Exception as e:
        print(f"Error: Failed to retrieve OTP, Error: {e}")
        raise


def enter_country_and_wait_for_options(driver, country_name, retries=3):
    """Enter the country name and ensure options appear."""
    COUNTRY_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter country name")')
    PAK_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pakistan (+92)")')

    for attempt in range(retries):
        print(f"Entering '{country_name}' in Country Field (Attempt {attempt + 1}/{retries})")
        wait_and_send_keys(driver, COUNTRY_FIELD, country_name)
        time.sleep(5)  # Wait for options to appear

        # Check if "Pakistan (+92)" appears in the options
        try:
            print("Checking if 'Pakistan (+92)' is visible...")
            WebDriverWait(driver, 10).until(EC.presence_of_element_located(PAK_FIELD))
            print("'Pakistan (+92)' is visible, clicking...")
            wait_and_click(driver, PAK_FIELD)
            return  # Exit once successful
        except Exception:
            print(f"Attempt {attempt + 1} failed: 'Pakistan (+92)' not visible yet. Retrying...")

            # Clear the field and retry if not successful
            country_input_element = WebDriverWait(driver, 10).until(EC.presence_of_element_located(COUNTRY_FIELD))
            country_input_element.clear()
            time.sleep(1)

    raise Exception(f"Failed to select '{country_name}' after {retries} attempts.")


def main():
    driver = set_up_appium()
    driver.implicitly_wait(10)

    try:
        LANG_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')
        LOGIN_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
        TEXT_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("🇸🇦")')
        COUNTRY_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Enter country name")')
        PAK_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pakistan (+92)")')
        PHONE_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone number")')
        LOGIN1_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
        AGREE_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Agree")')
        NEXT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
        NEXT2_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(2)')
        EDIT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Edit")')
        EDIT1_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Edit")')

        print("Clicking on Language Button")
        wait_and_click(driver, LANG_BUTTON)

        print("Clicking on Login Button")
        wait_and_click(driver, LOGIN_BUTTON)

        # Wait for 5 seconds after clicking the Login button
        print("Waiting for 5 seconds after clicking the Login button...")
        time.sleep(5)

        print("Clicking on Text Field (Flag)")
        wait_and_click(driver, TEXT_FIELD)
        time.sleep(3)

        print("Entering 'Pakistan' in Country Field")
        wait_and_send_keys(driver, COUNTRY_FIELD, 'Pakistan')
        time.sleep(5)

        print("Clicking on 'Pakistan (+92)'")
        wait_and_click(driver, PAK_FIELD)

        print("Entering phone number")
        wait_and_send_keys(driver, PHONE_FIELD, '3091431565')

        print("Clicking on Login Button")
        wait_and_click(driver, LOGIN1_BUTTON)

        print("Retrieving OTP from WhatsApp")
        retrieve_otp_from_whatsapp(driver)

        print("Clicking on Agree Button")
        wait_and_click(driver, AGREE_BUTTON)

        print("Clicking on Next Button")
        wait_and_click(driver, NEXT_BUTTON)

        print("Clicking on Second Next Button")
        wait_and_click(driver, NEXT2_BUTTON)

        print("Clicking on Edit Button")
        wait_and_click(driver, EDIT_BUTTON)

        print("Clicking on Edit 1 Button")
        wait_and_click(driver, EDIT1_BUTTON)

        print("Setting Date in the Picker")
        select_full_date(driver)

        print("Test execution complete.")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
