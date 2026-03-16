'''
Question 3 : Using ID and PARTIAL LINK TEXT
--> Open Amazon
--> Search for Mobiles (use ID)
--> Click on any 1 mobile (use PARTIAL LINK TEXT)
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option("detach", True)

driver = Chrome(options=o)

# Open Amazon
driver.get("https://www.amazon.in")

# Search for Mobiles (Using ID)
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.send_keys("mobiles")

driver.find_element(By.ID, "nav-search-submit-button").click()

sleep(3)

# Click any one mobile (Using PARTIAL LINK TEXT)
driver.find_element(By.PARTIAL_LINK_TEXT, "Samsung").click()

sleep(5)
driver.quit()
