from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time

countries = ['Canada', 'Germany', 'Iceland', 'Pakistan', 'Singapore', 'South Africa']

browser = webdriver.Chrome() # Get local session of firefox
browser.get("http://international.o2.co.uk/internationaltariffs/calling_abroad_from_uk") # Load page

for name in countries:

	elem = browser.find_element_by_id("countryName") # Find the query box
	elem.clear()
	elem.send_keys(name + Keys.RETURN)
	time.sleep(0.2) # Let the page load, will be added to the API

	code = browser.find_element_by_id("countryCode")
	print (name,"\t\t" , code.text);
browser.close()
