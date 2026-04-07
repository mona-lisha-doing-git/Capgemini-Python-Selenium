"""
SauceDemo Login
"""

import pytest
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By


@pytest.fixture(autouse=True)
def openAndClose():
    o = ChromeOptions()
    o.add_experimental_option('detach', True)
    global driver
    driver = Chrome(options=o)
    yield
    driver.quit()


@pytest.mark.parametrize("username, password, expected", [
    ("standard_user", "secret_sauce", "Products"),
    ("locked_out_user", "secret_sauce", "Epic sadface"),
    ("standard_user", "secret_s", "Epic sadface")
])
def test_login(username, password, expected):

    driver.get("https://www.saucedemo.com/")

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    page_source = driver.page_source

    assert expected in page_source
