from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"/Users/kapilnegi/Desktop/chromedriver")

driver.get("https://www.google.com")

driver.save_screenshot("save_screenshot_example.png")

driver.quit()
