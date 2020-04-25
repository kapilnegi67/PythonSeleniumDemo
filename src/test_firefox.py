from selenium import webdriver
import time


def test_for_firefox():
    driver = webdriver.Firefox(executable_path=r"/Users/kapilnegi/Desktop/geckodriver")

    driver.get("http://www.seleniumframework.com/demo-sites/")
    
    print("Page Title = ", driver.title)
    print("Current URL = ", driver.current_url)
    print("Page Source = ", driver.page_source)
    
    time.sleep(5)
    
    driver.quit()