from selenium import webdriver
import time

driver = webdriver.Chrome(executable_path=r"/Users/kapilnegi/Desktop/chromedriver")

# driver.get("http://www.seleniumframework.com/demo-sites/")
#
# print("Page Title = ", driver.title)
# print("Current URL = ", driver.current_url)
# print("Page Source = ", driver.page_source)



# driver.quit()

driver.get("https://www.icicibanks.com/")

time.sleep(5)

try:
    driver.find_element_by_id("push-modal-close").click()
except Exception:
    pass

time.sleep(5)

driver.quit()

