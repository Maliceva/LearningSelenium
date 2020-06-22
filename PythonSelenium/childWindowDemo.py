from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://the-internet.herokuapp.com/windows")

# This link opens a new browser tab (considered a child window)
driver.find_element_by_link_text("Click Here").click()

# In order for Selenium to see the contents of the new child window, you have to switch to it:
# driver.window_handles stores the child window IDs in a list: ("parentid", "childid")
childWindow = driver.window_handles[1]
parentWindow = driver.window_handles[0]

driver.switch_to.window(childWindow)
print (driver.find_element_by_tag_name("h3").text)

# Close the child window
driver.close()

# Switch back to the first window
driver.switch_to.window(parentWindow)

assert "Opening a new window" == driver.find_element_by_tag_name("h3").text


