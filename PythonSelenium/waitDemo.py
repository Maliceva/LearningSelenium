# Implicit wait - wait for the driver object to finish the current step of the test (globally applied)
# pause the test using the time class in Python
import time
from selenium import webdriver

driver = webdriver.Chrome(executable_path="/Users/cassandra.reitz/PycharmProjects/chromedriver")
driver.implicitly_wait(3) # maximum wait time for 3 seconds for each step (not 3 seconds for each step)
driver.get('https://rahulshettyacademy.com/seleniumPractise/#/')

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

# Enter promo code and click Apply
driver.find_element_by_class_name("promoCode").send_keys("rahulshettyacademy")
driver.find_element_by_css_selector(".promoBtn").click()

# Verify if the promo code was successfully applied
print(driver.find_element_by_css_selector("span.promoInfo").text)











