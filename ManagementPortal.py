import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Initialize WebDriver
driver = webdriver.Chrome()
wait = WebDriverWait(driver, 20)
driver.maximize_window()

# Visit the login page
time.sleep(10)
driver.get('https://dev-portal.ithnain.com/auth/login')

# Log in to the portal
time.sleep(5)
wait.until(EC.element_to_be_clickable((By.ID, 'login_email'))).send_keys("sameer.jahangir+superadmin@cloudpacer.com")
wait.until(EC.element_to_be_clickable((By.ID, 'login_password'))).send_keys("!7K@d@K@4a!7")
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()
time.sleep(5)

# Open modal
time.sleep(10)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ant-btn'))).click()

# # Navigate to the Users section
time.sleep(10)
wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.ant-menu-item-selected'))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, "//span[normalize-space()='Users']"))).click()
time.sleep(2)

# # Create a new user
time.sleep(3)
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='New User']"))).click()
wait.until(EC.element_to_be_clickable((By.ID, 'register_user_username'))).send_keys("1-1")
wait.until(EC.element_to_be_clickable((By.ID, 'register_user_email'))).send_keys("qa@cloudpacer.com")
time.sleep(5)

# Select country as Pakistan
# Click the flag dropdown
wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'flag-dropdown'))).click()

# Wait for the country list to be visible and then select 'Pakistan'
time.sleep(5)
try:
    country_option = wait.until(EC.presence_of_element_located((By.XPATH, "//ul[contains(@class, 'country-list')]//li[contains(., 'Pakistan')]")))
    driver.execute_script("arguments[0].scrollIntoView(true);", country_option)
    country_option.click()
    print("Clicked on the country option successfully.")
except Exception as e:
    print(f"Error occurred: {e}")

# Fill phone number
wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@placeholder='Enter your phone number']"))).send_keys("308556878")

# Assign user role
time.sleep(2)
try:
    role_input = wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@id='register_user_role']")))
    driver.execute_script("arguments[0].scrollIntoView(true);", role_input)
    role_input.click()
    print("Clicked on the role input successfully.")
except Exception as e:
    print(f"Error occurred: {e}")

wait.until(EC.element_to_be_clickable((By.XPATH, "//div[@class='ant-select-item-option-content'][normalize-space()='Admin']"))).click()

# # Assign user category
# time.sleep(5)
# wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='register_user_category']"))).click()
# wait.until(EC.element_to_be_clickable((By.CLASS_NAME, ".ant-select-item-option-content:contains('Patient Care')"))).click()
#
# # Assign entity
# time.sleep(5)
# wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@id='register_user_entityName']"))).click()
# wait.until(EC.element_to_be_clickable((By.CLASS_NAME, ".ant-select-item-option-content:contains('sameer hospital')"))).click()
#
# # Submit
# wait.until(EC.element_to_be_clickable((By.XPATH, "//span[normalize-space()='Confirm']"))).click()
# time.sleep(5)

# # Navigate to the Entities section and create a new entity
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-menu-item:contains('Entities')"))).click()
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-btn:contains('New Entity')"))).click()
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Enter entity name']"))).send_keys("Ithnain")
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Enter entity name in Arabic']"))).send_keys("Test1")
# wait.until(EC.element_to_be_clickable((By.ID, 'register_user_type'))).click()
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-select-item-option-content:contains('Hospital')"))).click()
# wait.until(EC.element_to_be_clickable((By.ID, 'register_user_access_type'))).click()
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".ant-select-item-option-content:contains('General Dashboard')"))).click()
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Enter entity Dashboard ID']"))).send_keys("123")
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "input[placeholder='Enter entity details dashboard ID']"))).send_keys("234")
# wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))).click()

# Other sections follow similarly...

# Pass the browser
pass
