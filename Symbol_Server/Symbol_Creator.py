from selenium import webdriver
from Symbol_Class import Symbol
from selenium.webdriver.common.keys import Keys

# Get input for quote
quote_to_get = input("Grab information for: ")

driver = webdriver.Firefox()
driver.get("http://finance.yahoo.com/q?s=")  # + str(quote_to_get))

search_box = driver.find_element_by_name('s')
search_box.send_keys(str(quote_to_get), Keys.RETURN)
