from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Set up the WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# Function to wait for an element to be clickable
def wait_for_element(xpath, timeout=10):
    return WebDriverWait(driver, timeout).until(EC.element_to_be_clickable((By.XPATH, xpath)))

try:
    # Visit the login page
    driver.get('https://dev-portal.ithnain.com/auth/login')

    # Log in to the portal
    wait_for_element("//input[@id='login_email']").send_keys("sameer.jahangir+superadmin@cloudpacer.com")
    wait_for_element("//input[@id='login_password']").send_keys("!7K@d@K@4a!7")
    wait_for_element("//button[@type='submit']").click()
    time.sleep(4)

    # Open modal
    wait_for_element('.ant-btn').click()

    # Navigate to the Users section
    wait_for_element('.ant-menu-item-selected').click()
    time.sleep(4)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Users')]").click()

    # Create a new user
    time.sleep(4)
    wait_for_element("//button[contains(text(), 'New User')]").click()
    wait_for_element("//input[@id='register_user_username']").send_keys("Maryam")
    wait_for_element("//input[@id='register_user_email']").send_keys("qa@cloudpacer.com")

    # Select country as Pakistan
    wait_for_element('.flag-dropdown').click()
    wait_for_element("//ul[contains(@class,'country-list')]//li[contains(text(), 'Pakistan')]").click()

    # Fill phone number
    wait_for_element("//input[@placeholder='Enter your phone number']").send_keys("308556878")

    # Assign user role
    wait_for_element("//input[@id='register_user_role']").click()
    wait_for_element("//div[@class='ant-select-item-option-content'][normalize-space()='Admin']").click()

    # Assign user category
    wait_for_element("//input[@id='register_user_category']").click()
    wait_for_element("//div[@class='ant-select-item-option-content'][normalize-space()='Patient Care']").click()

    # Assign entity
    wait_for_element("//input[@id='register_user_entityName']").click()
    wait_for_element("//div[@class='ant-select-item-option-content'][normalize-space()='sameer hospital']").click()

    # Submit
    wait_for_element("//button[@type='submit']").click()
    time.sleep(4)

    # Navigate to the Entities section and create a new entity
    time.sleep(4)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Entities')]").click()
    wait_for_element("//button[contains(text(), 'New Entity')]").click()
    wait_for_element("//input[@placeholder='Enter entity name']").send_keys("Test")
    wait_for_element("//input[@placeholder='Enter entity name in Arabic']").send_keys("Test1")
    wait_for_element("//div[@id='register_user_type']").click()
    wait_for_element("//div[@class='ant-select-item-option-content'][normalize-space()='Hospital']").click()
    wait_for_element("//div[@id='register_user_access_type']").click()
    wait_for_element("//div[@class='ant-select-item-option-content'][normalize-space()='General Dashboard']").click()
    wait_for_element("//input[@placeholder='Enter entity dashboard ID']").send_keys("123")
    wait_for_element("//input[@placeholder='Enter entity details dashboard ID']").send_keys("234")
    wait_for_element("//button[@type='submit']").click()
    time.sleep(4)

    # Navigate to Subscriptions and create a new subscription
    time.sleep(4)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Subscriptions')]").click()
    wait_for_element("//button[contains(text(), 'New Subscription')]").click()
    wait_for_element("//input[@id='register_package_userId']").click()
    wait_for_element("//div[@class='ant-select-item-option-content'][normalize-space()='257']").click()
    wait_for_element("//input[@id='register_package_coachId']").click()
    wait_for_element("//div[@class='ant-select-item-option-content'][normalize-space()='Charlie']").click()
    wait_for_element("//input[@id='register_package_packageId']").click()
    wait_for_element("//div[@class='ant-select-item-option-content'][normalize-space()='No Random Coach Package']").click()
    wait_for_element("//div[@class='ant-picker-input']").click()
    wait_for_element("//div[@class='ant-picker-cell-inner'][contains(text(),'20')]").click()
    wait_for_element("//button[@type='submit']").click()
    time.sleep(4)

    # Book a session
    time.sleep(1)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Sessions')]").click()
    wait_for_element("//button[contains(text(), 'Book Session')]").click()

    # Navigate to Payments section
    time.sleep(4)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Payments')]").click()

    # Create a new patient
    time.sleep(4)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Patients')]").click()
    wait_for_element("//button[contains(text(), 'New Patient')]").click()
    wait_for_element("//input[@id='register_patient_phoneNumber']").send_keys("+923069039296")
    wait_for_element("//input[@id='register_patient_entityName']").click()
    wait_for_element("//div[@class='ant-select-item-option-content'][normalize-space()='sameer hospital']").click()
    wait_for_element("//input[@id='register_patient_role']").click()
    wait_for_element("//div[@class='ant-select-item-option-content'][normalize-space()='Patient']").click()
    wait_for_element("//button[@type='submit']").click()
    time.sleep(4)

    # Navigate to Coaches and create a new coach
    time.sleep(4)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Coaches')]").click()
    # Add new coach if necessary:
    # wait_for_element("//button[contains(text(), 'New Coach')]").click()

    # Navigate to Forms, create a new form
    time.sleep(4)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Forms')]").click()
    wait_for_element("//button[contains(text(), 'Create a Form')]").click()

    # Navigate to Packages and create a new package
    time.sleep(4)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Packages')]").click()
    wait_for_element("//button[contains(text(), 'New Package')]").click()

    # Navigate to Referral Programs and create a new program
    time.sleep(4)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Referal Programs')]").click()
    wait_for_element("//button[contains(text(), 'New Program')]").click()

    # Navigate to Notification Center and create a new notification
    time.sleep(4)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Notification Center')]").click()
    wait_for_element("//button[contains(text(), 'Create New')]").click()

    # Navigate to Surveys and create a new survey
    time.sleep(4)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Surveys')]").click()
    wait_for_element("//button[contains(text(), 'New Survey')]").click()

    # Logout
    time.sleep(4)
    wait_for_element("//div[contains(@class,'ant-menu-item') and contains(text(),'Logout')]").click()
    wait_for_element("//button[contains(text(),'Logout')]").click()
    time.sleep(2)

finally:
    pass
