'''
Question 2 : Using Name
--> Open Facebook
--> Enter email and password
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option('detach', True)

driver = Chrome(options=o)

driver.get("https://www.facebook.com")

driver.find_element(By.NAME, "email").send_keys("abc@gmail.com")
driver.find_element(By.NAME, "pass").send_keys("abc@gmail.com")

sleep(5)

driver.close()
