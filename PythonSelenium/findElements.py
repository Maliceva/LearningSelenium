import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/cassandra.reitz/PycharmProjects/chromedriver")
driver.get("https://www.makemytrip.com")

# Open the From city drop down and start the autocomplete feature
driver.find_element_by_id("fromCity").click()
driver.find_element_by_css_selector("input[placeholder='From']").send_keys("del")
time.sleep(2) # wait after entering Del to let the list load

# All elements in the list belong to the blackText class, but have no unique identifier.
# Write custom CSS to find the unique list items: p[class*='blackText']
# Use find_elementS (plural) to get all and assign them to a list variable called cities
cities = driver.find_elements_by_css_selector("p[class*='blackText']")
# Get the number of elements in the list
print(len(cities))

# Cycle through the list of results and click on Del Rio
for city in cities:
    if city.text == "Del Rio, United States":
        city.click()
        break # stop looking for items in the list once Del Rio has been found and clicked

driver.find_element_by_xpath("//p[text()='Delhi, India']").click()
