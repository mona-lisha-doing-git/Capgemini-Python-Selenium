from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep
import time

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

'''
Assertion
'''
# 'Google'
# driver.implicitly_wait(10)
# driver.get("https://www.google.com")
# driver.maximize_window()
#
# # print(driver.title)
#
# expected = 'Google'
# actual = driver.title
#
# assert expected == actual, "Title mismatch"
#
# sleep(3)
# driver.quit()

# 'Amazon'
# driver.implicitly_wait(10)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
#
# driver.find_element(By.XPATH, "(//a[text()='Bestsellers'])[1]").click()
#
# expected = 'Amazon.in Bestsellers: The most popular items on Amazon'
# actual = driver.title
#
# assert expected == actual, "Title mismatch"
#
# sleep(3)
# driver.quit()

'''
Screenshot
'''
import os
# driver.implicitly_wait(10)
# driver.get("https://www.google.com")
#
# # driver.save_screenshot('ss1.png')
#
# folder = os.path.join(os.getcwd(), 'screenshot')
# os.makedirs(folder, exist_ok=True)
#
# 'Screenshot of the page'
# # driver.save_screenshot(f'{folder}/ss1.png')
#
# 'Screenshot of an element'
# ele = driver.find_element(By.XPATH, "//textarea[@title='Search']")
# # ele.screenshot(f'{folder}/ssElement.png')
#
# 'Using time stamp to make every name unique'
# timestamp = time.strftime("%Y%m%d-%H%M%S")
# ele.screenshot(f'{folder}/ssEl_{timestamp}.png')
#
# driver.quit()

'''
give valid username and invalid password
'''
# driver.implicitly_wait(10)
# driver.get("https://www.saucedemo.com")
# driver.maximize_window()
#
# driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('standard_user')
# driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('secret_sauc')
# driver.find_element(By.XPATH, "//input[@id='login-button']").click()
#
# folder = os.path.join(os.getcwd(), 'screenshot')
# os.makedirs(folder, exist_ok=True)
#
# expected = "Epic sadface: Username and password do not match any user in this service"
# actual = driver.find_element(By.XPATH, "//h3[@data-test='error']")
# timestamp = time.strftime("%Y%m%d-%H%M%S")
# assert expected == actual, driver.save_screenshot(f'{folder}/ss_{timestamp}.png')
#
# sleep(3)
# driver.quit()


o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.implicitly_wait(10)
driver.get("https://www.saucedemo.com")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys('standard_user')
driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys('secret_sauc')
driver.find_element(By.XPATH, "//input[@id='login-button']").click()

folder = os.path.join(os.getcwd(), 'screenshot')
os.makedirs(folder, exist_ok=True)

expected = "Epic sadface: Username and password do not match any user in this service"
actual = driver.find_element(By.XPATH, "//h3[@data-test='error']")
timestamp = time.strftime("%Y%m%d-%H%M%S")
assert expected == actual, driver.save_screenshot(f'{folder}/ss_{timestamp}.png')

sleep(3)
driver.quit()

