from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("https://login.salesforce.com/")

driver.find_element_by_css_selector("#username").send_keys("test@email.com")
driver.find_element_by_css_selector(".password").send_keys("password")
driver.find_element_by_css_selector(".password").clear() # deletes text from the form element

# Finds a link on the page with an a# tag that matches the text and clicks it
# Can also use find_element_by_partial_link_text - uses regex to find the link
driver.find_element_by_link_text("Forgot Your Password?").click()

# Finds an element based on the label on the page (not recommended as labels change a lot)
# Syntax: #//tagname[text()='xxx']
driver.find_element_by_xpath("//a[text()='Cancel']").click()

# Finds a child element based on the parent element ("Traversing tags")
# Xpath: //div[@id='usernamegroup']/label
   # You can traverse multiple parents: //form[@name='login']/div[1]/label
   # Test the selector in ChroPath to make sure you're identifying the right element
# CSS: div[id='usernamegroup'] label
print(driver.find_element_by_xpath("//form[@name='login']/div[1]/label").text)
print(driver.find_element_by_css_selector("form[name='login'] label:nth-child(3)").text)

# Relative vs. absolute xpath
# use Relative, absolute has a tendency to change and is less human readable

