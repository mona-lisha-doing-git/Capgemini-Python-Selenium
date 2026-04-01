from time import sleep

import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o = ChromeOptions()
o.add_experimental_option("detach", True)
driver = Chrome(options=o)

driver.get("https://demowebshop.tricentis.com/register")
driver.maximize_window()

driver.implicitly_wait(15)

@pytest.mark.regression
def test_gender():
    driver.find_element(By.XPATH, "//input[@id='gender-female']").click()

def test_name():
    driver.find_element(By.XPATH, "//input[@id= 'FirstName']").send_keys("Monalisha")

def test_lastname():
    driver.find_element(By.XPATH, "//input[@id= 'LastName']").send_keys("Kalita")

def test_email():
    driver.find_element(By.XPATH, "//input[@id= 'Email']").send_keys("monalisha@gmail.com")

def test_pass():
    driver.find_element(By.XPATH, "//input[@id= 'Password']").send_keys("123456")

def test_cnfmPass():
    driver.find_element(By.XPATH, "//input[@id= 'ConfirmPassword']").send_keys("123456")

def test_regbtn():
    driver.find_element(By.ID, "register-button").click()

sleep(5)
driver.close()
