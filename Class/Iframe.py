# 24-03-2026 (Tuesday)

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.implicitly_wait(15)
driver.get("file:///Users/monalishakalita/Downloads/untitled folder/iframe.html")
driver.maximize_window()

driver.find_element(By.ID, "inp1").send_keys("First Input")

'Using index'
# driver.switch_to.frame(0)
'Using name'
# driver.switch_to.frame('n1')
'Using id'
driver.switch_to.frame('frame1')
driver.find_element(By.ID, "inp2").send_keys("Second Input")

'Using index'
# driver.switch_to.frame(0)
'Using name'
# driver.switch_to.frame('n2')
'Using id'
driver.switch_to.frame('frame2')
driver.find_element(By.ID, "inp3").send_keys("Third Input")

sleep(10)
driver.quit()
