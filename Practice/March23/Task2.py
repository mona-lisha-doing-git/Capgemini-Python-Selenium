'''
Launch Nike
using action chains
perform mouse hover action on kids after sometime perform click action on that
give a scroll(by amount or anything)
and then click on shop
pick anyone shoe and give a click
after that click on add to bag and select a size and then click add to bag
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)

driver = Chrome(options=o)

# Launched Nike Website
driver.implicitly_wait(15)
driver.get("https://www.nike.in")
driver.maximize_window()

actions = ActionChains(driver)

# Mouse hover on Kids section and then after sometime clicked it
kids = driver.find_element(By.XPATH, "//span[text()='Kids']")
actions.move_to_element(kids).perform()
sleep(3)

kids.click()

# Driver to next window
driver.switch_to.window(driver.window_handles[1])

# Scroll and click the shop Button
actions.scroll_by_amount(0,500).perform()

driver.find_element(By.XPATH, "//a[text()='Shop']").click()

# Scroll to the shoe and click it
shoe = driver.find_element(By.XPATH, "(//div[@class = 'css-1sjxv95'])[13]")
sleep(1)
actions.scroll_to_element(shoe).perform()
sleep(2)
shoe.click()

# Driver to next window
driver.switch_to.window(driver.window_handles[2])

# Size selected and added to bag
driver.find_element(By.XPATH, "//label[text()='UK 6 (EU 40)']").click()
sleep(1)
driver.find_element(By.XPATH, "//button[text()='Add to Bag']").click()

sleep(10)
driver.quit()
