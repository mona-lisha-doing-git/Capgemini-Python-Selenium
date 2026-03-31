"""
Write a script to:

1) navigate to amazon
2) search a product through send_keys BUT dont click on search icon
3) Wait for the suggestions to appear
4) Click on 4th suggestion
5) Click on Sort By and click on newest
6) Click on free shipping check box
7) wait for first product and return the name=price
"""

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# Launch amazon
driver.implicitly_wait(15)
driver.get("https://www.amazon.in")
driver.maximize_window()

# Search for a Product
driver.find_element(By.ID, 'twotabsearchtextbox').send_keys('shoes')
sleep(1)

# Click on the forth option
driver.find_element(By.XPATH, "//div[@class='left-pane-results-container']//div[@aria-rowindex='4']").click()

# Click on Sort by
driver.find_element(By.XPATH, "//span[text()='Sort by:']").click()

# Click on Newest
driver.find_element(By.XPATH, "//a[text()='Newest Arrivals']").click()

# Click on Fee Shipping checkbox
driver.find_element(By.XPATH, "(//i[@class='a-icon a-icon-checkbox'])[3]").click()

# Print first appearing product name=price
name = driver.find_element(By.XPATH, "((//div[@data-cy='asin-faceout-container'])[1]//h2)[2]//span")
price = driver.find_element(By.XPATH, "//div[@data-cy='asin-faceout-container']//div[@class='a-row']//span[@class='a-price-whole']")

print(f"First appeared product with price is: {name.text} = {price.text}")

sleep(2)
driver.quit()
