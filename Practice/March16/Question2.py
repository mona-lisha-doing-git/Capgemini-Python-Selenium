"""
1. Open Flipkart
2. Search for Mobiles
3. Click on the search button
4. Select any mobile and fetch its price using XPATH and print it
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://www.flipkart.com/")
driver.maximize_window()
sleep(1)

driver.find_element(By.XPATH, "//span[@role='button']").click()
sleep(2)

driver.find_element(By.CLASS_NAME, "nw1UBF.v1zwn25").send_keys("Mobiles")
sleep(2)

driver.find_element(By.XPATH, '//button[@type="submit"]').click()
sleep(2)

driver.find_element(By.XPATH, "(//div[@class='hZ3P6w DeU9vF'])[1]").click()
print(driver.find_element(By.XPATH, "(//div[@class='hZ3P6w DeU9vF'])[1]").text)

sleep(5)
driver.quit()
