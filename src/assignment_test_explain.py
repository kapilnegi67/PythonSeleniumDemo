my_options = driver.find_elements_by_xpath("//ul[@role='listbox']//li//span")

# my_options = [webelement1, web2, web3, web4]

for my_ele in my_options:
    print("Option Text = ", my_ele.text)
    if my_ele.text == "facebook search":
        my_ele.click()

my_links = driver.find_elements_by_xpath("//div[@class='g']//a")

for link in my_links:
    if "www.facebook.com" in link.get_attribute("href"):
        print("PASS")
        
        
        
        
        
        
print(driver.find_element_by_xpath("//div[@qa='product_name']//a").text)

my_products = driver.find_elements_by_xpath("//div[@qa='product_name']//a")

my_products[1].text