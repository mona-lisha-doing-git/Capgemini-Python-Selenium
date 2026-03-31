"""
Write a Selenium script to open a website take screenshots.

1) Open https://in.pinterest.com/
2) Take the screenshot of entire page
3) Scroll to a picture and capture the screenshot of the picture
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import os
import time

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# Launched Pinterest Website
driver.implicitly_wait(10)
driver.get("https://in.pinterest.com/")
driver.maximize_window()

# Generating a folder for screenshots if not present
folder = os.path.join(os.getcwd(), 'screenshot')
os.makedirs(folder, exist_ok=True)

# Timestamp for uniqueness and screenshot of the page
timestamp = time.strftime("%Y%m%d-%H%M%S")
driver.save_screenshot(f'{folder}/page_screenshot_{timestamp}.png')

actions = ActionChains(driver)

# Scroll to the element
img = driver.find_element(By.XPATH, "(//img[@class='iFOUS5 ALBw9Q'])[12]")
actions.scroll_to_element(img).perform()

# Screenshot of the element
img.screenshot(f'{folder}/element_screenshot.{timestamp}.png')

sleep(3)
driver.quit()
