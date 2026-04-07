import time
from time import sleep

import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


@pytest.fixture(scope="class")
def setup():
    o = ChromeOptions()
    o.add_experimental_option("detach", True)
    driver = Chrome(options=o)

    driver.get("https://demowebshop.tricentis.com/register")
    driver.maximize_window()

    time.sleep(2)
    yield driver
    driver.close()


class Test_Register:

    # driver = setup
    def test_gender(self, setup):
        setup.find_element(By.XPATH, "//input[@id='gender-female']").click()
        sleep(1)


    def test_name(self, setup):
        setup.find_element(By.XPATH, "//input[@id= 'FirstName']").send_keys("Monalisha")
        sleep(1)


    def test_lastname(self, setup):
        setup.find_element(By.XPATH, "//input[@id= 'LastName']").send_keys("Kalita")
        sleep(1)


    def test_email(self, setup):
        setup.find_element(By.XPATH, "//input[@id= 'Email']").send_keys("monalisha@gmail.com")
        sleep(1)


    def test_pass(self, setup):
        setup.find_element(By.XPATH, "//input[@id= 'Password']").send_keys("123456")
        sleep(1)


    def test_cnfmPass(self, setup):
        setup.find_element(By.XPATH, "//input[@id= 'ConfirmPassword']").send_keys("123456")
        sleep(1)


    def test_regbtn(self, setup):
        setup.find_element(By.ID, "register-button").click()
        sleep(1)
