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
    options.set_capability('appPackage', 'com.ithnain_patient_app')
    options.set_capability('appActivity', 'com.ithnain_patient_app.MainActivity')
    options.set_capability('uiautomator2ServerLaunchTimeout', 60000)

    return webdriver.Remote("http://127.0.0.1:4723", options=options)


def wait_and_click(driver, locator, timeout=20):
    """Wait for an element to be clickable and then click it."""
    element = WebDriverWait(driver, timeout).until(EC.element_to_be_clickable(locator))
    element.click()


def wait_and_send_keys(driver, locator, text, timeout=20):
    """Wait for an element to be present and then send keys to it."""
    element = WebDriverWait(driver, timeout).until(EC.presence_of_element_located(locator))
    element.send_keys(text)


def main():
    driver = set_up_appium()
    driver.implicitly_wait(10)

    try:
        # Constants for element locators
        LANG_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("English")')
        ACCOUNT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Create new account")')
        TEXT_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("🇸🇦")')
        COUNTRY_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("text-input-country-filter")')
        PAK_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Pakistan (+92)")')
        PHONE_FIELD = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Phone Number")')
        TERMS_CHECKBOX = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("RNE__ICON__Component")')
        SIGNUP_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Signup")')
        VERIFICATION_CODE_FIELD = lambda fn: (By.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("textInput").instance({fn})')
        EDIT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().instance(0)')
        DATE_PICKER = lambda text: (By.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}")')
        MONTH_PICKER = lambda text: (By.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}")')
        YEAR_PICKER = lambda text: (By.ANDROID_UIAUTOMATOR,f'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView(new UiSelector().text("{text}")')
        OK_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("android:id/button1")')
        MEDICAL_REFERRAL = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Through a medical referral.")')
        MEDICAL_REFERRAL_CODE = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Type your medical referral code.")')
        NEXT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(1)')
        I_AM_PATIENT = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("I am the patient")')
        PATIENT_NAME = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Write patient name.")')
        MALE_GENDER = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Male")')
        NEXT2_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().className("com.horcrux.svg.PathView").instance(2)')
        DIABETES_TYPE1 = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Type 1 diabetes")')
        CHECKBOX = lambda fn: (By.ANDROID_UIAUTOMATOR, f'new UiSelector().resourceId("RNE__Checkbox__Icon").instance({fn})')
        GOAL_SELECT = lambda text, fn: (By.ANDROID_UIAUTOMATOR, f'new UiSelector().text("{text}").instance({fn})')
        SUBMIT_BUTTON = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("submit")')
        NOT_NOW = (By.ANDROID_UIAUTOMATOR, 'new UiSelector().text("NOT NOW")')

        # Click on Language Button
        wait_and_click(driver, LANG_BUTTON)

        # Click on Login Button
        wait_and_click(driver, ACCOUNT_BUTTON)

        # Click on Text Field
        wait_and_click(driver, TEXT_FIELD)

        # Send keys to Country Field and select Pakistan
        wait_and_send_keys(driver, COUNTRY_FIELD, 'Pakistan')
        wait_and_click(driver, PAK_FIELD)

        # Send keys to Phone Number Field
        wait_and_send_keys(driver, PHONE_FIELD, '3068001018')

        # Check Terms and Conditions
        wait_and_click(driver, TERMS_CHECKBOX)

        # Click on Signup Button
        wait_and_click(driver, SIGNUP_BUTTON)

        # Enter verification code
        for idx, digit in enumerate('1234'):
            wait_and_send_keys(driver, VERIFICATION_CODE_FIELD(idx), digit)

        # Click on Edit Button
        wait_and_click(driver, EDIT_BUTTON)

        # Select Date
        wait_and_click(driver, DATE_PICKER("29"))
        wait_and_click(driver, MONTH_PICKER("Jul"))
        wait_and_click(driver, YEAR_PICKER("2023"))

        # Click on OK Button
        wait_and_click(driver, OK_BUTTON)

        # Click on Medical Referral
        wait_and_click(driver, MEDICAL_REFERRAL)
        wait_and_send_keys(driver, MEDICAL_REFERRAL_CODE, '4884')

        # Click on Next Button
        wait_and_click(driver, NEXT_BUTTON)

        # Select "I am the patient" option
        wait_and_click(driver, I_AM_PATIENT)

        # Send keys to Patient Name
        wait_and_send_keys(driver, PATIENT_NAME, 'AHMAD')

        # Select Male Gender
        wait_and_click(driver, MALE_GENDER)

        # Click on Next Button
        wait_and_click(driver, NEXT2_BUTTON)

        # Select Type 1 Diabetes
        wait_and_click(driver, DIABETES_TYPE1)

        # Click on Next Button
        wait_and_click(driver, NEXT2_BUTTON)

        # Click on Edit Button
        wait_and_click(driver, EDIT_BUTTON)

        # Select Date
        wait_and_click(driver, DATE_PICKER("2"))
        wait_and_click(driver, MONTH_PICKER("Jun"))
        wait_and_click(driver, YEAR_PICKER("2023"))

        # Click on OK Button
        wait_and_click(driver, OK_BUTTON)

        # Click on Next Button
        wait_and_click(driver, NEXT2_BUTTON)

        # Check checkboxes
        for idx in range(3):
            wait_and_click(driver, CHECKBOX(idx))

        # Click on Next Button
        wait_and_click(driver, NEXT2_BUTTON)

        # Select goals
        goals = [("Carb Counting", 0), ("Weight Loss", 0), ("Weight Loss", 1), ("Reduce Diabetes", 0)]
        for goal_text, instance_idx in goals:
            wait_and_click(driver, GOAL_SELECT(goal_text, instance_idx))

        # Click on others button and send keys
        wait_and_click(driver, GOAL_SELECT("others", 0))
        wait_and_send_keys(driver, GOAL_SELECT("Write your goal", 0), 'Major Goal')

        # Click on submit button
        wait_and_click(driver, SUBMIT_BUTTON)

        # Click on Not Now button
        wait_and_click(driver, NOT_NOW)

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
