from selenium.webdriver import Chrome, ChromeOptions
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in")
