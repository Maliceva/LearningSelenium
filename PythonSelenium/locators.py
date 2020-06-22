# Validating form elements on https://rahulshettyacademy.com/angularpractice
# Get values and attributes from inspecting the page and hovering over the element you want to validate
# Note: you can only use values that are exposed by the web developer (ex: if Name is missing, use ID)
# Note: use Chropath Chrome extension to quickly get Xpath and CSS syntax (Dev tools -> Elements tab >> Cropath)
# Webdriver locators:
# ID - find_element_by_id (python) findElementByID (Java)
# Name - findElementByName
# XPath
# CSS - FASTEST way to locate elements
# Class name
# Link text


from selenium import webdriver
from selenium.webdriver.support.select import Select
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://rahulshettyacademy.com/angularpractice")

# Types "Cassandra" into the Name field
driver.find_element_by_name("name").send_keys("Cassandra")
driver.find_element_by_name("email").send_keys("cass.reitz@gmail.com")

# Checks the "Check me out if you Love IceCreams!" checkbox
driver.find_element_by_id("exampleCheck1").click()

# Uses the CSS selector to find the element
# Validate CSS in browser console first by using the following syntax: $("input[name='name']")
driver.find_element_by_css_selector("input[name='name']").send_keys(" Reitz")

# Drop down menu locator (static, no autofill) - select class requires you to create an object and import at the top
dropdown = Select(driver.find_element_by_id("exampleFormControlSelect1"))
dropdown.select_by_visible_text("Female")
dropdown.select_by_index(0) # selects the first option (Male)
#dropdown.select_by_value("M") # selects based on value, if present

# Uses the XPath to find the element
# Validate XPath in browser console first using the following syntax: $x("//input[@type='submit']")
#Clicks the Submit button to send the form
driver.find_element_by_xpath("//input[@type='submit']").click()

# Grab confirmation text and determine if it's present
# This has multiple classes - to isolate it in Chropath, use regular expressions: [class*='alert-success'] or for xpath //*[contains(@class,'alert-success')]
message = driver.find_element_by_class_name("alert-success").text
# Assert expects this to be true, if not the test fails:
# Check for part of the text:
assert "success" in message
# Match the text exactly:
#assert "Success! The Form has been submitted successfully!" == message

#assert "asdfjklsdf" in message





