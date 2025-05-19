from appium import webdriver
from appium.options.common import AppiumOptions

# Set up Appium options
options: AppiumOptions = AppiumOptions()
options.set_capability('platformName', 'iOS')
options.set_capability('platformVersion', '16.4')
options.set_capability('deviceName', 'iPhone 14 Pro Max')
options.set_capability('browserName', 'safari')
options.set_capability('automationName', 'XCUITest')
options.set_capability('udid', '48D9A17D-406F-475F-8CCA-499D035F03AD')  # Replace with your device UDID if using a real device
options.set_capability('xcodeOrgId', 'Maryam Waheed (Personal Team)')  # Replace with your Apple developer team ID
options.set_capability('xcodeSigningId', 'iPhone Developer')
options.set_capability('useNewWDA', True)  # Ensures a new WDA session is created
options.set_capability('wdaStartupRetries', 4)  # Number of times to retry starting WDA
options.set_capability('wdaStartupRetryInterval', 20000)  # Interval between retries in milliseconds
options.set_capability('wdaLaunchTimeout', 120000)
options.set_capability('webviewConnectTimeout', 30000)
# Initialize Appium driver
driver = webdriver.Remote("http://127.0.0.1:4723", options=options)

# Quit the driver
driver.quit()
