# Automated Test Software
'''from selenium.webdriver import Chrome
from time import sleep

driver = Chrome()
sleep(5)'''

'''from selenium.webdriver import Edge
from time import sleep

driver = Edge()
sleep(5)'''

from time import sleep
from selenium.webdriver import Chrome,ChromeOptions

o=ChromeOptions() # ChromeOptions is another class
o.add_experimental_option("detach", False) # telling the chrome browser to not close the window after launching

driver = Chrome(options=o) # driver variable is holding the chrome browser
driver.get('https://demoqa.com')
# driver.get('https://www.google.com')

# Browser Window methods
# driver.maximize_window()
# sleep(2)
# driver.minimize_window()
# sleep(3)
# driver.fullscreen_window()

# To fetch the title
title = driver.title
# print(title)
# print(driver.current_url)
# print(driver.page_source)

sleep(3)
driver.close()
# driver.quit()

