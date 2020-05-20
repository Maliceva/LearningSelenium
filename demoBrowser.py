from selenium import webdriver
# Browser exposes an executable file
# Through Selenium test, we need to invoke the executable file which will then invoke the actual browser
driver = webdriver.Chrome(executable_path="/Users/cassandra.reitz/PycharmProjects/chromedriver")

driver.get("https://www.shoebacca.com/") # Go to a specific site