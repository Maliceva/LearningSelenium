# Explicit wait - target a specific element and only wait for it to load
# Must be applied individually, is not global

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/cassandra.reitz/PycharmProjects/chromedriver")
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

wait = WebDriverWait(driver, 5) # Pass driver and number of seconds to wait

# Search for items on the webstore, then add them to the cart
driver.find_element_by_css_selector("input.search-keyword").send_keys("berry")
time.sleep(4) # wait for the products to be filtered
productCount = len(driver.find_elements_by_xpath("//div[@class='products']/div"))
print (productCount)
assert productCount == 2 # Two products should be returned - Strawberry and Raspberry

# Get all the "Add to Cart" buttons for the products returned by the search and click them
addToCartButtons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in addToCartButtons:
    button.click()

# Open the cart and proceed to checkout page
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# Only wait a maximum of 5 seconds for the promoCode to appear
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

# Enter promo code and click Apply
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

# Wait a maximum of 5 seconds for the success message to be displayed
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,"span.promoInfo")))

# Verify if the promo code was successfully applied
print(driver.find_element_by_css_selector("span.promoInfo").text)











