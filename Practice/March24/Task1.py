'''

'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# driver.implicitly_wait(15)
# driver.get("https://x.com")
# driver.maximize_window()
#
# # driver.switch_to.iframe(0)
# driver.find_element(By.XPATH, "//span[text() = 'Sign up with Google']").click()
#
# sleep(10)
# driver.quit()

driver.implicitly_wait(15)
driver.get("https://www.zomato.com/jaipur/restaurants")
driver.maximize_window()

# driver.switch_to.iframe(0)
driver.find_element(By.XPATH, "//a[text()='Log in']").click()

sleep(10)
driver.quit()
