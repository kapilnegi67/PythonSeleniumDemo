from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"/Users/kapilnegi/Desktop/chromedriver")

driver.get("http://demo.guru99.com/popup.php")

driver.maximize_window()

driver.find_element_by_xpath("//*[contains(@href,'popup.php')]").click()

windows = driver.window_handles

for window in windows:
    driver.switch_to.window(window)
    try:
        driver.find_element_by_name("emailid").send_keys("kapil@gmail.com")
        driver.find_element_by_name("btnLogin").click()
    except Exception:
        pass
    driver.close()


driver.quit()
