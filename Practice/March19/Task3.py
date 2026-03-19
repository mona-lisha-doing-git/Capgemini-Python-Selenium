from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

'''
Demo Web shop
'''
driver.implicitly_wait(15)
driver.get("https://demowebshop.tricentis.com/")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
driver.find_element(By.XPATH, "//input[@id='gender-female']").click()
driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("Monalisha")
driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("Kalita")
driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("monalisha@gmail.com")
driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("mypassword")
driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("mypassword")
driver.find_element(By.XPATH, "//input[@id='register-button']").click()

sleep(10)
driver.quit()