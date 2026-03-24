"""
 Open three websites in separate tabs
 Print each tab's title and url
 Close all except the first tab
"""

from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.implicitly_wait(15)
driver.get("https://www.google.com")
driver.maximize_window()

# 'Website 1'
driver.switch_to.new_window()
driver.get("https://www.myntra.com")

# 'Website 2'
driver.switch_to.new_window()
driver.get("https://demoqa.com")

# 'Website 3'
driver.switch_to.new_window()
driver.get("https://www.amazon.in")

for i in range(3):
    n = len(driver.window_handles) - 1
    driver.switch_to.window(driver.window_handles[n])
    sleep(2)
    print("Title: ", driver.title)
    print("Current URL: ", driver.current_url)
    driver.close()

driver.switch_to.window(driver.window_handles[0])
print("Title: ", driver.title)
print("Current URL: ", driver.current_url)

sleep(3)
driver.quit()
