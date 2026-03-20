# 20-03-2026

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver = Chrome(options=o)

'''
INTRODUCTION 
'''

'''
Select dropdown
'''
# driver.get("file:///Users/monalishakalita/Downloads/E22_Dropdowns.html")
# driver.maximize_window()

'''
# Select by visible text
'''

# dropdown = driver.find_element(By.ID, "state")
# option = Select(dropdown)

'''
# Select by index
'''
# option.select_by_index(1)

'''
# Select by value
'''
# option.select_by_value('MH')

# sleep(2)
# option.deselect_by_value("Badminton")
# option.deselect_all()

'''
Amazon website dropdown: Custom Dropdown
'''
driver.implicitly_wait(15)
driver.get("https://www.amazon.in/")
driver.maximize_window()

driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("Shoes for men")

sleep(2)
options = driver.find_elements(By.XPATH, "//div[@class='s-suggestion-container']")

for i in options:
    print(i.text)

# driver.find_element(By.XPATH, "(//div[@class='s-suggestion-container'])[10]").click()
options[9].click()

sleep(10)
driver.quit()
