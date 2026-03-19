from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

'''
The Internet
'''
driver.get("https://the-internet.herokuapp.com/checkboxes")
driver.maximize_window()

driver.implicitly_wait(15)

cb1 = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
print("Selected:", cb1.is_selected())
cb2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]")
print("Enabled:", cb2.is_enabled())

driver.quit()
