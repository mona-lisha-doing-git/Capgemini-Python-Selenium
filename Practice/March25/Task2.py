"""
Write a Selenium script in Python to open the Lenskart website,

1) open the
2) Click on Eyeglasses
3) Validate the url using assert
4) Locate the Sort By and select the option “Most Viewed”
5) Capture a screenshot of the webpage and save it to your local system
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep
import os

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# Launch Lenskart Website
driver.implicitly_wait(10)
driver.get("https://www.lenskart.com")
driver.maximize_window()

# Click on Eyeglasses
driver.find_element(By.ID, 'lrd1').click()

# Validate using assert
expected = "https://www.lenskart.com/eyeglasses.html"
actual = driver.current_url
assert expected == actual, "current_url mismatched"

# Located the dropdown and selected 'Most Viewed' using index
dropdown = driver.find_element(By.XPATH, "//label[text()='Sort By']/following::select")

option = Select(dropdown)

option.select_by_index(5)

# Screenshot of the page
folder = os.path.join(os.getcwd(), 'screenshot')
driver.save_screenshot(f'{folder}/lenskart_page_screenshot.png')

sleep(3)
driver.quit()
