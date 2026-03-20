'''
Click on English
click from station
to station
get details
'''
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver = Chrome(options=o)

driver.implicitly_wait(20)
driver.get("https://www.bmrc.co.in/")
driver.maximize_window()

driver.find_element(By.XPATH, "//span[text()='English']").click()

option1 = Select(driver.find_element(By.XPATH, "(//select[@class='form-control select fare-selects'])[1]"))
option1.select_by_index(3)

option2 = Select(driver.find_element(By.XPATH, "(//select[@class='form-control select fare-selects'])[2]"))
option2.select_by_index(5)

driver.find_element(By.XPATH, "//button[@class='app-btn-box']").click()

sleep(15)
driver.quit()
