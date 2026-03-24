"""
Launch Zomato and click login
Switch to a frame and perform some action
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.implicitly_wait(15)
driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()

driver.find_element(By.XPATH, "//a[text()='Log in']").click()

iframe = driver.find_element(By.ID, "auth-login-ui")

driver.switch_to.frame(iframe)

driver.find_element(By.XPATH, "//span[contains(text(),'Send One Time Password')]").click()

sleep(5)
driver.quit()
