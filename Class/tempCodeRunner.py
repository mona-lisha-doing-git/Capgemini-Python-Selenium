from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)

driver = Chrome(options=o)

driver.get("file:///Users/monalishakalita/Downloads/example.html")
driver.maximize_window()

'''
Get all <li> under Section 1
(//ul)[1]/child::li
'''

'''
Get all <a> inside container
//div[@id='container']//a
'''

'''
From Item 1, go to its <li>
//a[@id='link1']/parent::li
'''

'''
From footerLink, go to container
//a[@id='footerLink']/ancestor::div[@id='container']
'''

'''
From Item 2, get Item 3
(//a)[2]/following::a[1]
'''

'''
From Item 3, get Item 2
(//a)[3]/preceding::a[1]
'''

print(driver.name)

sleep(2)
driver.quit()
