from appium import webdriver
from appium.options.common import AppiumOptions

# Set up Appium options
options: AppiumOptions = AppiumOptions()
options.set_capability('platformName', 'iOS')
options.set_capability('platformVersion', '16.7.8')
options.set_capability('deviceName', ' iPhone 8 Plus')
options.set_capability('app', 'safari')
options.set_capability('automationName', 'XCUITest')
options.set_capability('udid', 'c0ee8b9db03974d77739d5e494a7dd2eafa92cd3')  # Replace with your device UDID if using a real device
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
