from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By # we generally on import by, keys and action change
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# Implicit wait and explicit wait

driver.get("https://the-internet.herokuapp.com/dynamic_loading/1")
driver.maximize_window()
# driver.implicitly_wait(15)
driver.find_element(By.XPATH, "//button").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id='finish']/h4")))
txt = driver.find_element(By.XPATH, "//div[@id='finish']/h4")

print(txt.text)

driver.quit()

# mini classwork 1
# driver.implicitly_wait(10)
# driver.get("https://www.decathlon.in/")
# driver.maximize_window()
# driver.find_element(By.XPATH, "//a[contains(@href,'https://www.decathlon.in/shop/Winter-Collection')]").click()
