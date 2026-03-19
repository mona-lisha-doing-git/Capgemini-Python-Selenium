from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in")
sleep(2)

# Task 1
print(driver.title)

# Task 2
print(driver.current_url)

# Task 3
driver.get("https://www.wikipedia.org")

driver.refresh()
print(driver.title)
sleep(1)

driver.get("https://www.amazon.in")

print(driver.title)
sleep(2)
driver.back()

# Done and closing all the windows
sleep(5)
driver.quit()
