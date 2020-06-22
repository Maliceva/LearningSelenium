# JavaScript DOM can access any elements on a webpage just like Selenium
# Selenium has a method to execute Javascript code in it
# This comes in handy when you're unable to locate something using Selenium

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://rahulshettyacademy.com/angularpractice")

# Enter text in a Name field
driver.find_element_by_name("name").send_keys("Cassandra")

# If you want to display the text entered by Selenium, .text won't work:
print(driver.find_element_by_name("name").text) # this returns nothing

# Instead, use get_attribute:
print(driver.find_element_by_name("name").get_attribute("value"))

# Execute JavaScript command inside the webdriver to get the same result:
print(driver.execute_script('return document.getElementsByName("name")[0].value'))

# Locate an element using Selenium but click on it with JS
shopButton = driver.find_element_by_css_selector("a[href*='shop']")
driver.execute_script("arguments[0].click();", shopButton)

# Selenium doesn't support scrolling up or down within the browser, but JS does
# If you're trying to click an element that is not visible due to scrolling, use JS
# Scroll from top of the screen to the bottom:
driver.execute_script("window.scrollTo(0,document.body.scrollHeight);")
