from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

driver.implicitly_wait(15)
driver.get("https://testautomationpractice.blogspot.com")
driver.maximize_window()

driver.find_element(By.XPATH, "//input[@id='singleFileInput']").send_keys(r"/Users/monalishakalita/Downloads/demo.jpg")

driver.find_element(By.XPATH, "//input[@id='multipleFilesInput']").send_keys("//Users//monalishakalita//Downloads//demo.jpg\n", "//Users//monalishakalita//Downloads//demo1.jpg")

sleep(10)
# driver.quit()
