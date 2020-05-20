from selenium import webdriver
# Browser exposes an executable file
# Through Selenium test, we need to invoke the executable file which will then invoke the actual browser
# Download drivers from https://www.selenium.dev/downloads/ and save them somewhere, then pass in the filepath:
#driver = webdriver.Chrome(executable_path="/Users/cassandra.reitz/PycharmProjects/chromedriver") # Chrome
#driver = webdriver.Firefox(executable_path="/Users/cassandra.reitz/PycharmProjects/geckodriver") # Firefox
driver = webdriver.Safari(executable_path="/usr/bin/safaridriver") # Safari


driver.get("https://www.shoebacca.com/") # Go to a specific site

print(driver.title) # Return the title of the page
print(driver.current_url) # Return the URL you landed on
driver.get("https://rahulshettyacademy.com/AutomationPractice") # goes to a different site
driver.maximize_window() # sets the current browser window to maximum size
driver.minimize_window() # minimizes the current browser window
driver.back() # returns to shoebacca.com from the new url
driver.refresh() # reloads the current page

driver.close() # Close the invoked browser in the current window