from selenium import webdriver

driver = webdriver.Chrome(executable_path=r"/Users/kapilnegi/Desktop/chromedriver")
driver.get("https://demoqa.com/")

element = driver.find_element_by_link_text("Selectable")
element.click()

select_list = driver.find_element_by_id("selectable")
select_list.find_element_by_xpath("//li[text()='Item 1']").click()

print(select_list.find_element_by_xpath("//li[text()='Item 1']").get_attribute("class"))

driver.quit()