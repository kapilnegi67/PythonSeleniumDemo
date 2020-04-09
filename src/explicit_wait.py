from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path=r"/Users/kapilnegi/Desktop/chromedriver")

driver.get("https://www.facebook.com/" )

try:
    element = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.NAME, "websubmit")))
    element.click()
except Exception:
    pass

driver.quit()
