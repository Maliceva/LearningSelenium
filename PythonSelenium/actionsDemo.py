# Working with mega menus (menu items are only displayed on mouseover)
# ActionChains class allows you to do more advanced actions

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains

driver = webdriver.Chrome(ChromeDriverManager().install())

#driver.get("https://www.familysearch.org/en/")

# Declare ActionChains before use
action = ActionChains(driver)

# Moves the cursor to the specified element ("Search" menu item)
#action.move_to_element(driver.find_element_by_xpath("//button[@aria-controls='search']")).perform()

# Click on the "Genealogies" menu item that appears on mouseover under "Search"
#action.move_to_element(driver.find_element_by_xpath("//a[@data-test='genealogies']")).click().perform()


# Demonstrating double click actions
# driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
# action.double_click(driver.find_element_by_id("double-click")).perform()

# Double clicking the button opens an alert. We need to make sure it worked and close the alert:
# alert = driver.switch_to.alert
# assert "You double clicked me!!!, You got to be kidding me" == alert.text
# alert.accept()

# Right click example:
# action.context_click(driver.find_element_by_id("double-click")).perform()

# Demonstrating hidden/displayed actions
driver.get("https://rahulshettyacademy.com/AutomationPractice/")

# Element is displayed by default, should be true
assert (driver.find_element_by_css_selector("#displayed-text").is_displayed())

# Hide the element
driver.find_element_by_id("hide-textbox").click()

# Element should be hidden now, should be false
assert not (driver.find_element_by_css_selector("#displayed-text").is_displayed())
