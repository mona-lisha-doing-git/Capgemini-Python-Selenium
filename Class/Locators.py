# 13-03-2026 (Friday)

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# Enter field values in demoqa and click submit
'''
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
# driver.find_element(By.ID, 'userName').send_keys('abc')
username = driver.find_element(By.ID, "userName")
username.send_keys("abc")
sleep(2)
useremail = driver.find_element(By.ID, "userEmail")
useremail.send_keys("abc@gmail.com")
sleep(2)
currAddress = driver.find_element(By.ID, "currentAddress")
currAddress.send_keys("Jaipur, Rajasthan")
sleep(2)
pmAddress = driver.find_element(By.ID, "permanentAddress")
pmAddress.send_keys("Guwahati, Assam")
sleep(2)
driver.find_element(By.ID,'submit').click()
'''

# Open amazon --> search for shirts --> click search
'''
driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(2)
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('shirts')
sleep(1)
driver.find_element(By.ID, 'nav-search-submit-button').click()
sleep(3)
driver.close()
'''

# Pass values in demoq using class name, everyone having the same class name will only hold the first element
'''
driver.get('https://demoqa.com/text-box')
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME, 'mr-sm-2.form-control').send_keys("Monalisha")
sleep(5)
driver.close()
'''

# Pass values in demoq using tag name(least used locator)
'''
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(1)
driver.find_element(By.TAG_NAME, 'input').send_keys("Monalisha")
sleep(2)
driver.close()
'''

# Link Text (include every space, case sensitive)
'''
driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(1)
driver.find_element(By.LINK_TEXT, 'Mobiles').click()
sleep(2)
driver.back()
sleep(5)
driver.close()
'''

# Partial Link Text
'''
driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(1)
driver.find_element(By.PARTIAL_LINK_TEXT, 'Kitchen').click()
sleep(2)
driver.back()
sleep(5)
driver.close()
'''

#
'''
driver.get('https://www.amazon.in')
driver.maximize_window()
sleep(1)
driver.find_element(By.CSS_SELECTOR, '').send_keys("hoodies")
sleep(2)
driver.back()
sleep(5)
driver.close()
'''

