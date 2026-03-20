# 19-03-2026 (Thursday)

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)
#
# driver.get("https://www.google.com")
# driver.maximize_window()
#
# driver.implicitly_wait(15)
#
# links = driver.find_elements(By.TAG_NAME, 'a')
#
# # print(len(links))
#
# for i in links:
#     print(i.text)

'''
Amazon: Search --> return number of objects displayed
'''
# driver.get("https://www.amazon.in")
# driver.maximize_window()
#
# driver.implicitly_wait(15)

# search_box = driver.find_element(By.ID, "twotabsearchtextbox")
# search_box.send_keys("ipad")
#
# driver.find_element(By.ID, "nav-search-submit-button").click()

# all_product = driver.find_elements(By.CLASS_NAME, 'puisg-col-inner')
# print(len(all_product))

# count = 0
# for i in all_product:
#     count+=1
#     if count == 5:
#         print(i.text)
#         break

'Print all the navbar shop links'
# ele = driver.find_elements(By.XPATH, "//a[@class='nav-a  ']")
#
# for i in ele:
#     print(i.get_attribute('href'))

# driver.quit()

'''
is_enabled()
is_selected()
is_displayed()
'''

# driver.get("https://www.facebook.com/")
# driver.maximize_window()
#
# driver.implicitly_wait(15)
# ele = driver.find_element(By.XPATH, "//div[@aria-label='Log in']")
# print("Displayed:",ele.is_displayed())
# print("Enabled:",ele.is_enabled())
#
# btn = driver.find_element(By.XPATH, "//input[@type='submit']")
# print("\nDisplayed:",btn.is_displayed())
# print("Enabled:",btn.is_enabled())
#
# driver.quit()

'''
Naukri.com
'''
# driver.get("https://www.naukri.com/registration/createAccount?othersrcp=22636")
# driver.maximize_window()
#
# driver.implicitly_wait(15)
#
# btn = driver.find_element(By.XPATH, "//button[@type='submit']")
# print("\nDisplayed:",btn.is_displayed())
# print("Enabled:",btn.is_enabled())
#
# driver.quit()

'''
The Internet
'''
# driver.get("https://the-internet.herokuapp.com/checkboxes")
# driver.maximize_window()
#
# driver.implicitly_wait(15)
#
# cb1 = driver.find_element(By.XPATH, "//input[@type='checkbox'][1]")
# print("Selected:",cb1.is_selected())
# cb2 = driver.find_element(By.XPATH, "//input[@type='checkbox'][2]")
# print("Enabled:",cb2.is_enabled())
#
# driver.quit()

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

'''
Demo Web shop
'''
# driver.implicitly_wait(15)
# driver.get("https://demowebshop.tricentis.com/")
# driver.maximize_window();
#
# driver.find_element(By.XPATH, "//a[@class='ico-register']").click()
# driver.find_element(By.XPATH, "//input[@id='gender-female']").click()
# driver.find_element(By.XPATH, "//input[@id='FirstName']").send_keys("Monalisha")
# driver.find_element(By.XPATH, "//input[@id='LastName']").send_keys("Kalita")
# driver.find_element(By.XPATH, "//input[@id='Email']").send_keys("monalisha@gmail.com")
# driver.find_element(By.XPATH, "//input[@id='Password']").send_keys("mypassword")
# driver.find_element(By.XPATH, "//input[@id='ConfirmPassword']").send_keys("mypassword")
# driver.find_element(By.XPATH, "//input[@id='register-button']").click()
#
# sleep(10)
# driver.quit()
