from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option('detach', True)

driver = Chrome(options=o)

driver.get("https://www.amazon.in")

driver.find_element(By.ID, "glow-ingress-line2").click()

sleep(5)

driver.close()
