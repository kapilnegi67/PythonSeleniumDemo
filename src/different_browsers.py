from selenium import webdriver
import time

browser = "chrome"

if browser.lower() == "chrome":
    driver = webdriver.Chrome(executable_path=r"/Users/kapilnegi/Desktop/chromedriver")
elif browser.lower() == "safari":
    driver = webdriver.Safari()
else:
    driver = webdriver.Firefox(executable_path=r"/Users/kapilnegi/Desktop/geckodriver")

driver.get("http://www.seleniumframework.com/demo-sites/")

print("Page Title = ", driver.title)
print("Current URL = ", driver.current_url)
print("Page Source = ", driver.page_source)

time.sleep(5)

driver.quit()