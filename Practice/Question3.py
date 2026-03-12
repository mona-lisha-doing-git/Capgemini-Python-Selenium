from time import sleep
from selenium.webdriver import Chrome, ChromeOptions

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# Question 3
'''
Open Wikipedia
Refresh
Fetch Title
Open Amazon
Fetch Title
Go Back
Close
'''

driver.get("https://www.wikipedia.org")
driver.refresh()

driver.get('https://www.amazon.in')
sleep(3)
print(driver.title)
sleep(5)
driver.back()
sleep(2)
driver.close()
