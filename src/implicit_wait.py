from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"/Users/kapilnegi/Desktop/chromedriver")
driver.implicitly_wait(10)
driver.get("https://www.facebook.com/" )
driver.find_element_by_name("websumit").click()

driver.quit()
