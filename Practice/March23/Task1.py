'''
Test Automation Practice
mouse hover action
double click on copy text
drag and drop
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)

driver = Chrome(options=o)

driver.get("https://testautomationpractice.blogspot.com/")

actions = ActionChains(driver)

hover = driver.find_element(By.XPATH, "//button[text()='Point Me']")
double_click = driver.find_element(By.XPATH, "//button[text()='Copy Text']")
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")

actions.scroll_to_element(droppable).perform()
sleep(1)

# Hover
actions.move_to_element(hover).perform()

# Double click
actions.double_click(double_click).perform()

# Drag and Drop
actions.pause(3).drag_and_drop(draggable, droppable).perform()

sleep(10)
driver.quit()
