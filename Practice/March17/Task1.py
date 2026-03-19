from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By # we generally on import by, keys and action change
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

'''
Flipkart print the 6th result
'''

driver.get("https://www.flipkart.com")
driver.maximize_window()

wait = WebDriverWait(driver, 10)
wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@role='button']"))).click()
wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder]'))).send_keys("laptops")
wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='XFwMiH']"))).click()

txt = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='RG5Slk'])[6]")))
print(txt.text)

driver.quit()
