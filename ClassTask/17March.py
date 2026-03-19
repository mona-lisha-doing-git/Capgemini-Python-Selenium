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

# driver.get("https://www.flipkart.com")
# driver.maximize_window()
#
# wait = WebDriverWait(driver, 10)
# wait.until(EC.element_to_be_clickable((By.XPATH, "//span[@role='button']"))).click()
# wait.until(EC.visibility_of_element_located((By.XPATH, '//input[@placeholder]'))).send_keys("laptops")
# wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@class='XFwMiH']"))).click()
#
# txt = wait.until(EC.visibility_of_element_located((By.XPATH, "(//div[@class='RG5Slk'])[6]")))
# print(txt.text)
#
# driver.quit()

'''
# demoqa --> add then fetch that particular name and print name = salary
'''
driver.get("https://demoqa.com/webtables")
driver.maximize_window()


wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='addNewRecordButton']"))).click()

wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='First Name']"))).send_keys('Hello')
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Last Name']"))).send_keys('World')
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='name@example.com']"))).send_keys('monalisha@gmail.com')
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Age']"))).send_keys('20')
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Salary']"))).send_keys('23000')
wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@placeholder='Department']"))).send_keys('Finance')

wait.until(EC.visibility_of_element_located((By.XPATH, "//button[@id='submit']"))).click()

# name = wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text()='Hello']/..//td[5]")))
# salary = wait.until(EC.visibility_of_element_located((By.XPATH, "//td[text()='Hello']/..//td[5]")))

name = wait.until(EC.visibility_of_element_located((By.XPATH, "(//td)[22]")))
salary = wait.until(EC.visibility_of_element_located((By.XPATH, "(//td)[26]")))

print(f"{name.text} = {salary.text}")
