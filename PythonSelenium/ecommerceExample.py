# Explicit wait - target a specific element and only wait for it to load
# Must be applied individually, is not global
# Use when you know a particular process will take a while (waiting for filters to be applied, for example)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/Users/cassandra.reitz/PycharmProjects/chromedriver")
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

wait = WebDriverWait(driver, 5) # Pass driver and number of seconds to wait
addedToCartList = [] # Create an empty list for use later
cartPageList = []

# Search for items on the webstore, then add them to the cart
driver.find_element_by_css_selector("input.search-keyword").send_keys("berry")
time.sleep(4) # wait for the products to be filtered
productCount = len(driver.find_elements_by_xpath("//div[@class='products']/div"))

print("Product Count:")
print(productCount)
assert productCount == 2 # Two products should be returned - Strawberry and Raspberry

# Grab the product text and add the item to cart
addToCartButtons = driver.find_elements_by_xpath("//div[@class='product-action']/button")
for button in addToCartButtons:
    # Start searching from where the "Add to Cart" button is found (xpath only)
    # //div[@class='product-action']/button/parent::div/parent::div/h4 becomes: parent::div/parent::div/h4
    addedToCartList.append((button.find_element_by_xpath("parent::div/parent::div/h4").text))
    button.click()

print("Products added to cart:")
print(addedToCartList)

# Open the cart and proceed to checkout page
driver.find_element_by_css_selector("img[alt='Cart']").click()
driver.find_element_by_xpath("//button[text()='PROCEED TO CHECKOUT']").click()

# Only wait a maximum of 5 seconds for the promoCode to appear
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoCode")))

# Get Product names from the cart page and compare them against the products you clicked on
cart = driver.find_elements_by_css_selector("p.product-name")
for items in cart:
    cartPageList.append(items.text)

print("Products in cart:")
print(cartPageList)

# Test fails if items added to cart are not found inside the cart
assert addedToCartList == cartPageList

# Enter promo code and click Apply
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

# Wait a maximum of 5 seconds for the success message to be displayed
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "span.promoInfo")))

# Verify if the promo code was successfully applied
print(driver.find_element_by_css_selector("span.promoInfo").text)











