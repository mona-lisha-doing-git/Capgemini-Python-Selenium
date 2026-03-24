# 14-03-2026 (Saturday - Assessment Day so no Practice Task)

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# XPath using attribute and XPath using text
'''
driver.get("https://demoqa.com/text-box")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH, "//input[@placeholder='Full Name']").send_keys("Monalisha Kalita")
sleep(1)
driver.find_element(By.XPATH, "//input[@placeholder='name@example.com']").send_keys("mona@gmail.com")
sleep(1)
driver.find_element(By.XPATH, "//textarea[@placeholder='Current Address']").send_keys("Jaipur")
sleep(1)
driver.find_element(By.XPATH, "//textarea[@id='permanentAddress']").send_keys("Home")
sleep(1)
driver.find_element(By.XPATH, "//button[text()='Submit']").click()

sleep(5)
driver.quit()
'''

# 16-03-2026 (Monday)

'''
Fetching dynamic elements in demoqa
'''
# driver.get("https://demoqa.com/webtables")
# driver.maximize_window()
# salary = driver.find_element(By.XPATH, "//td[text()='Vega']/..//td[5]")
# print(f"Salary of Cierra: {salary.text}") # .text is a property
#
# department = driver.find_element(By.XPATH, "//td[text()='Vega']/..//td[6]")
# print(f"Department of Cierra: {department.text}")
#
# sleep(5)
# driver.quit()

'''
Fetching dynamic element
'''
# driver.get("https://the-internet.herokuapp.com/tables")
# driver.maximize_window()
# due = driver.find_element(By.XPATH, "//td[text()='Bach']/..//td[4]")
# print(f"Due of Bach Frank: {due.text}") # .text is a property
#
# sleep(5)
# driver.quit()

'''
Fetching dynamic element: following sibling and preceding sibling
'''
# driver.get("https://the-internet.herokuapp.com/tables")
# driver.maximize_window()
# due = driver.find_element(By.XPATH, "(//td[text()='Tim'])[1]//following-sibling::td[2]")
# print(f"Due of Tim: {due.text}")
#
# sleep(5)
# driver.quit()

'''
Open Amazon
Search for mobiles -> click on search icon
use mobile name -> fetch its price
'''
# driver.get("https://www.amazon.in")
# driver.maximize_window()
# sleep(2)
# driver.find_element(By.ID, 'twotabsearchtextbox').send_keys("Mobile")
# sleep(1)
# driver.find_element(By.ID, 'nav-search-submit-button').click()
# sleep(1)
# # driver.find_element(By.XPATH, "//span[contains(text(), 'iPhone 16 Plus 128 GB')][1]").click()
# # sleep(1)
# print("Price: ",driver.find_element(By.XPATH, "(//span[text()='₹'])[4]//following-sibling::span").text)
#
# sleep(10)
# driver.quit()

'''
Flipkart
'''
driver.get("https://www.flipkart.com")
driver.maximize_window()
sleep(2)

driver.find_element(By.XPATH, "//span[@role='button']").click()
sleep(2)
driver.find_element(By.XPATH, '//input[@placeholder]').send_keys("basketball")
sleep(2)
driver.find_element(By.XPATH, "//button[@class='XFwMiH']").click()

sleep(5)
driver.quit()
