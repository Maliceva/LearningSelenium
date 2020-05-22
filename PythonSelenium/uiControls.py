# Use a generic locator to perform a test on all elements of a page at once (click all checkboxes)

from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/cassandra.reitz/PycharmProjects/chromedriver")
driver.get('https://rahulshettyacademy.com/AutomationPractice/')

# Get all checkboxes on the page
checkboxes = driver.find_elements_by_xpath("//input[@type='checkbox']")
# Return the count of checkboxes
print(len(checkboxes)) # 3

# Loop through the checkboxes on the page, then click the one that says "option 2"
for checkbox in checkboxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected() # Validates that checkboxes were clicked

radioButtons = driver.find_elements_by_name("radioButton")
radioButtons[2].click()
assert radioButtons[2].is_selected() # Validates that radio button 3 was selected