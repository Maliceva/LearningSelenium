# Puts text into a WYSIWYG editor located inside an iframe
# Works for elements inside iframe, frameset and frame tags
# driver.switch_to.frame accepts frameID, frame name or index value

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get("http://the-internet.herokuapp.com/iframe")

driver.switch_to.frame("mce_0_ifr")


# Clear the WYSIWYG editor text and replace it with new text
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("This text was put here by my automated test")

# Switch out of the iframe back to the main page
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)