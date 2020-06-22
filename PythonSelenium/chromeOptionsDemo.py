# ChromeOptions class allows you to set the behavior of your browser

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--start-maximized") # creates a maximized window when loading the browser
chrome_options.add_argument("headless") # runs tests in the background instead of displaying the browser
chrome_options.add_argument("--ignore-certificate-error") # proceed even if certificate is expired

# You must pass the chrome_options when declaring the driver
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

driver.get("https://rahulshettyacademy.com/angularpractice")

print(driver.title)