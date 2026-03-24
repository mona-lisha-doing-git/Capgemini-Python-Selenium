"""
Open internet heroku website --> Javascript Alert
Click the alert buttons and whatever inside the alerts, print that too and click on ok button
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.implicitly_wait(15)
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.maximize_window()

# JS Alert Button, Simple Alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Alert']").click()
alert1 = driver.switch_to.alert
print(alert1.text)
sleep(1)
alert1.accept()
sleep(1)

# JS Confirm Button, Confirmation Alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Confirm']").click()
alert2 = driver.switch_to.alert
print(alert2.text)
sleep(1)
alert2.accept()
sleep(1)

# JS Prompt Button, Prompt Alert
driver.find_element(By.XPATH, "//button[text()='Click for JS Prompt']").click()
alert3 = driver.switch_to.alert
alert3.send_keys("Monalisha")
print(alert3.text)
sleep(1)
alert3.accept()
sleep(1)

sleep(2)
driver.quit()
