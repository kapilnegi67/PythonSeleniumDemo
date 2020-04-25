import pytest
from selenium import webdriver

test_data = [["user1", "pass1"],
             ["user2", "pass2"],
#              ["user3", "pass3"],
#              ["user4", "pass4"],
#              ["user5", "pass5"],
#              ["user6", "pass6"],
             ]
 
@pytest.mark.parametrize("username, password", test_data)
def test_login(username, password):
    driver = webdriver.Chrome(executable_path=r"/Users/kapilnegi/Desktop/chromedriver")
    driver.get("https://the-internet.herokuapp.com/login")
    driver.find_element_by_id("username").clear()
    driver.find_element_by_id("username").send_keys(username)
    driver.find_element_by_id("password").clear()
    driver.find_element_by_id("password").send_keys(password)

    # If username and password are correct
    # user lands on homepage
    # driver.quit()



# test_filename.py
# filename_test.py

# ABC.py

# src/test_filename.py
# src/filename_test.py
# src/ABC.py

# pytest ABC.py


