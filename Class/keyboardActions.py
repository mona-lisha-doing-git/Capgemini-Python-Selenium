# 23-03-2026 (Monday)

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.common.actions.wheel_input import ScrollOrigin

from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)

driver = Chrome(options=o)

'''
Use Keys.ENTER in amazon search bar
'''
# driver.implicitly_wait(15)
# driver.get("https://www.amazon.in/")
#
# driver.maximize_window()
#
# ele = driver.find_element(By.ID, 'twotabsearchtextbox')
# ele.send_keys("Shoes")
# ele.send_keys(Keys.ENTER)

'''
Demoqa/text-box: Enter current address and copy that to permanent address
'''
# driver.implicitly_wait(15)
# driver.get("https://demoqa.com/text-box")

# ele1 = driver.find_element(By.ID, 'currentAddress')
# ele1.send_keys("Jaipur")
# ele1.send_keys(Keys.CONTROL + 'A')
# ele1.send_keys(Keys.CONTROL + 'C')
#
# ele2 = driver.find_element(By.ID, 'permanentAddress')
# ele2.send_keys(Keys.CONTROL + 'V')

# sleep(10)
# driver.quit()


'''
Action Chains
'''
# driver.implicitly_wait(20)
# driver.get("https://demoqa.com/buttons")
# driver.maximize_window()
#
# ' Object Created '
# single_click = driver.find_element(By.XPATH, "//button[text()='Click Me']")
#
# ' Action Stored '
# actions = ActionChains(driver)
#
# ' Just stores the action '
# # actions.click(single_click)
#
# ' Now action is being performed '
# actions.click(single_click).perform()
#
# double_click = driver.find_element(By.XPATH, "//button[text()='Double Click Me']")
# actions.double_click(double_click).perform()
#
# right_click = driver.find_element(By.XPATH, "//button[text()='Right Click Me']")

'''
Scroll Action Chains
'''
# driver.implicitly_wait(20)
# driver.get("https://www.amazon.in/")
# driver.maximize_window()
#
# actions = ActionChains(driver)

# ele1 = driver.find_element(By.XPATH, "//div[contains(@class, 'a-cardui _quad-multi-asin-card-v2_fluid_fluidCard__3hmFA')]")
# ele = driver.find_element(By.XPATH, "(//div[contains(@class, 'a-cardui _quad-multi-asin-card-v2_fluid_fluidCard')])[4]")
# actions.scroll_to_element(ele1).pause(3).perform()
# actions.scroll_by_amount(0,900).pause(2).perform()

# # origin = ScrollOrigin.from_viewport(0, 0)
# origin = ScrollOrigin.from_element(ele1)
# actions.scroll_from_origin(origin, 0, 900).pause(2).perform()

'hover'
# ele2 = driver.find_element(By.XPATH, "//div[@id='nav-link-accountList']")
# actions.move_to_element(ele2).perform()

# sleep(15)
# driver.quit()

'''
Yono Bank - Click and hold
'''

# driver.implicitly_wait(10)
# driver.get("https://yonobusiness.sbi.bank.in/yonobusinesslogin")
# driver.maximize_window()
#
# actions = ActionChains(driver)
#
# driver.find_element(By.XPATH, "//span[@class='ng-tns-c2785778308-3 icon-cancel']").click()
# ele = driver.find_element(By.ID, 'password').send_keys("Hello World")
# btn = driver.find_element(By.XPATH, "//div[@class='addIcon']/button")
# actions.click_and_hold(btn).pause(3).release().perform()
#
# sleep(10)
# driver.quit()


'''
Demoqa: Drag and Drop
'''
# driver.implicitly_wait(10)
# driver.get("https://demoqa.com/droppable")
# driver.maximize_window()
#
# actions = ActionChains(driver)
#
# item = driver.find_element(By.ID, "draggable")
# dest = driver.find_element(By.ID, "droppable")
#
# actions.pause(2).drag_and_drop(item, dest).perform()
#
# sleep(10)
# driver.quit()

'''
Tabs and windows
'''
driver.implicitly_wait(15)
driver.get("https://www.google.com")
driver.maximize_window()

sleep(5)

# manually open 3 tabs
print(driver.current_window_handle)
print("Before:", driver.title)

driver.switch_to.new_window()

driver.get("https://www.amazon.in/")
sleep(2)

print(driver.window_handles)
print("After:", driver.title)

driver.switch_to.window(driver.window_handles[0])
sleep(2)
driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("world")

sleep(10)
driver.quit()
