from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

'''
Demoqa
'''

driver.implicitly_wait(15)
driver.get("https://demoqa.com/automation-practice-form")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@placeholder='First Name']").send_keys("Monalisha")
driver.find_element(By.XPATH, "//input[@placeholder='Last Name']").send_keys("Kalita")
driver.find_element(By.XPATH, "//input[@placeholder='name@example.com']").send_keys("monalisha@gmail.com")
driver.find_element(By.XPATH, "//input[@value='Female']").click()
driver.find_element(By.XPATH, "//input[@placeholder='Mobile Number']").send_keys("1234567890")
driver.find_element(By.XPATH, "//input[@id='dateOfBirthInput']").click()
driver.find_element(By.XPATH, "//div[@aria-label='Choose Wednesday, March 18th, 2026']").click()
driver.find_element(By.XPATH, "//input[@id='subjectsInput']").send_keys("Python Selenium")
driver.find_element(By.XPATH, "//input[@id='hobbies-checkbox-1']").click()
driver.find_element(By.XPATH, "//input[@id='hobbies-checkbox-2']").click()

driver.find_element(By.XPATH, "//input[@id='uploadPicture']").click()
driver.find_element(By.XPATH, "//textarea[@placeholder='Current Address']").send_keys("Jaipur")
# State
# driver.find_element(By.XPATH, "//div[@class = 'css-1xc3v61-indicatorContainer'][1]").click()
# City
# driver.find_element(By.XPATH, "//div[@class = 'css-1xc3v61-indicatorContainer'][1]").send_keys("monalisha@gmail.com")


sleep(10)
driver.quit()