"""
1. Open Amazon
2. Search for Mobiles
3. Click on search icon
4. Use mobile name, & fetch its price(using XPATH)
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.amazon.in")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("Mobiles")
sleep(1)
driver.find_element(By.ID, 'nav-search-submit-button').click()
sleep(1)

# 'Printing the price'
print(driver.find_element(By.XPATH, '//h2[contains(.,"Samsung Galaxy S26 Ultra 5G (Black, 12GB RAM, 256GB Storage)")]/../../..//span[contains(@class,"a-price-whole")]').text)

sleep(10)
driver.quit()
