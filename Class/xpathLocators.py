# 14-03-2026 (Friday)

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# XPath using attribute and XPath using text
'''
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Full Name']").send_keys("Monalisha Kalita")
sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='name@example.com']").send_keys("mona@gmail.com")
sleep(1)
driver.find_element(By.XPATH, "//textarea[@placeholder='Current Address']").send_keys("Jaipur")
sleep(1)
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("Home")
sleep(1)
driver.find_element(By.XPATH, "//button[text()='Submit']").click()

sleep(5)
driver.quit()
'''

#
