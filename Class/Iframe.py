# 24-03-2026 (Tuesday)

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# driver.implicitly_wait(15)
# driver.get("file:///Users/monalishakalita/Downloads/untitled folder/iframe.html")
# driver.maximize_window()
#
# driver.find_element(By.ID, "inp1").send_keys("First Input")

'Using index'
# driver.switch_to.frame(0)
'Using name'
# driver.switch_to.frame('n1')
'Using id'
# driver.switch_to.frame('frame1')
# driver.find_element(By.ID, "inp2").send_keys("Second Input")

'Using index'
# driver.switch_to.frame(0)
'Using name'
# driver.switch_to.frame('n2')
'Using id'
# driver.switch_to.frame('frame2')
# driver.find_element(By.ID, "inp3").send_keys("Third Input")

'Switch to parent frame'
# driver.switch_to.parent_frame()
# inp2 = driver.find_element(By.ID, 'inp2')
# inp2.clear()
# inp2.send_keys("I am back")

'Switch to parent frame'
# driver.switch_to.parent_frame()
# inp1 = driver.find_element(By.ID, 'inp1')
# inp1.clear()
# inp1.send_keys("I am back")

'Switch to default content'
# driver.switch_to.default_content()
# page1 = driver.find_element(By.ID, 'inp1')
# page1.clear()
# page1.send_keys("This is the default page.")
#
# sleep(10)
# driver.quit()


'''
X.com: switch to the iframe and click sign up with google
'''

# driver.implicitly_wait(15)
# driver.get("https://x.com")
# driver.maximize_window()
#
# driver.switch_to.frame(0)
# driver.find_element(By.XPATH, "//span[text() = 'Sign up with Google']").click()
#
# sleep(5)
# driver.quit()

'''
Alerts and Pop ups
'''
# driver.implicitly_wait(15)
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
#
# actions = ActionChains(driver)
# ele = driver.find_element(By.XPATH, "//button[text()='Popup Windows']")
# actions.scroll_to_element(ele).perform()

# 'Simple Alert'
# simple_alert = driver.find_element(By.ID, "alertBtn")
# simple_alert.click()
# sleep(2)
# alert1 = driver.switch_to.alert
# alert1.accept()

# 'Confirmation Alert'
# confirm_alert = driver.find_element(By.ID, "confirmBtn")
# confirm_alert.click()
# sleep(2)
# alert2 = driver.switch_to.alert
# # alert2.accept()
# alert2.dismiss()

# 'Prompt Alert'
# prompt_alert = driver.find_element(By.ID, "promptBtn")
# prompt_alert.click()
# sleep(2)
# alert3 = driver.switch_to.alert
# alert3.send_keys("Monalisha")
# alert3.accept()
#
# sleep(10)
# driver.quit()

'''
Python: Download (Safe browsing)
'''
# driver.implicitly_wait(15)
# o.add_experimental_option("prefs", {"safebrowsing.enabled":True})
# driver = Chrome(options=o)
#
# driver.implicitly_wait(15)
# driver.get("https://www.python.org/downloads/")
# driver.maximize_window()
#
# actions = ActionChains(driver)
# driver.find_element(By.XPATH, "(//a[contains(text(),'Download Python')])[3]").click()
#
# sleep(10)
# driver.quit()

'''
Disable Notification
'''
o.add_argument("--disable-notifications")
driver = Chrome(options=o)

driver.implicitly_wait(15)
driver.get("https://www.easemytrip.com")
driver.maximize_window()

sleep(5)
driver.quit()
