'''
Open flipkart
Perform scroll action to the bottom of the page(scroll to myntra)
click myntra, switch back to flipkart
click Clearstrip, switch back to flipkart
click shopsee, switch back to flipkart
print all the tabs
print all the id, title, url of all tabs
'''

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)

driver = Chrome(options=o)

# Opened Flipkart
driver.implicitly_wait(15)
driver.get("https://www.flipkart.com")
driver.maximize_window()

actions = ActionChains(driver)

driver.find_element(By.XPATH, "//span[@class='b3wTlE']").click()

# Scroll to the footer (At the bottom of the page) and click Myntra, Cleartrip and Shopsy
actions.scroll_to_element(driver.find_element(By.TAG_NAME, 'footer'))

# Myntra
myntra = driver.find_element(By.XPATH, "((//div[@class='ykJuJZ'])[2]/following::a)[1]")
actions.scroll_to_element(myntra).perform()
sleep(2)
myntra.click()

driver.switch_to.window(driver.window_handles[0])

# Cleartrip
cleartrip = driver.find_element(By.XPATH, "((//div[@class='ykJuJZ'])[2]/following::a)[2]")
actions.scroll_to_element(cleartrip).perform()
sleep(2)
cleartrip.click()

driver.switch_to.window(driver.window_handles[0])

# Shopsy
shopsy = driver.find_element(By.XPATH, "((//div[@class='ykJuJZ'])[2]/following::a)[3]")
actions.scroll_to_element(shopsy).perform()
sleep(2)
shopsy.click()

driver.switch_to.window(driver.window_handles[0])

for i in range(4):
    driver.switch_to.window(driver.window_handles[i])
    print("ID:", driver.current_window_handle)
    print("Title:", driver.title)
    print("Current URL:", driver.current_url)
    print()

sleep(2)

sleep(10)
driver.quit()
