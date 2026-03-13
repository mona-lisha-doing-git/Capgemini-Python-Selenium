# 13-03-2026 (Friday)

'''
1. Go to https://Selenium.dev/
2. Click on 'Downloads' - (link text)
3. Click on 'Other Pages exist' - (partial link text)
4. Fetch title
'''
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
driver.get("https://selenium.dev/")
sleep(1)
driver.maximize_window()
sleep(2)
driver.find_element(By.LINK_TEXT, 'Downloads').click()
sleep(2)
driver.find_element(By.PARTIAL_LINK_TEXT, 'other languages exist').click()
sleep(5)
driver.close()
