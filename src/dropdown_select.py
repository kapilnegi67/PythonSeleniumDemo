from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver = webdriver.Chrome(executable_path=r"/Users/kapilnegi/Desktop/chromedriver")

driver.get("http://demo.guru99.com/test/newtours/register.php")

drpCountry = Select(driver.find_element_by_name("country"))

drpCountry.select_by_visible_text("ANTARCTICA")

# Selecting Items in a multiple select elements

driver.get("http://jsbin.com/osebed/2")

fruits = Select(driver.find_element_by_id("fruits"))

assert fruits.is_multiple

fruits.select_by_visible_text("Banana")

fruits.deselect_by_visible_text("Banana")

fruits.deselect_by_visible_text("Apple")

fruits.select_by_index(1)

driver.quit()
