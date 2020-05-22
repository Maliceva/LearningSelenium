# Enter text into a box, click Alert, then validate that the alert message includes the text you submitted
# Alerts are not handled by the Selenium driver - use the alert function
# alert.text grabs the text from the popup
# alert.accept() clicks OK
# alert.dismiss() clicks Cancel
# You have to use driver.switch_to.alert to access these methods


from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/cassandra.reitz/PycharmProjects/chromedriver")
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Enter a name and click "Alert"
validateText = "Cassandra"
driver.find_element_by_id("name").send_keys(validateText)
driver.find_element_by_id("alertbtn").click()

# Enable the ability to see the alert popup
alert = driver.switch_to.alert
alertText = alert.text
assert validateText in alertText #Check to see if the text you entered is present in the alert
alert.accept() # Clicks OK to close the alert