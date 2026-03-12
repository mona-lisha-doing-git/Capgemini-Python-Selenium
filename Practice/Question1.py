from selenium.webdriver import Chrome, ChromeOptions

o=ChromeOptions()
o.add_experimental_option('detach', True)
driver = Chrome(options=o)

# Question 1
driver.get("https://www.google.com")
print(driver.title)
