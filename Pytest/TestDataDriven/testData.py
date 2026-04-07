"""
SauceDemo Login
"""

import pytest
from selenium.webdriver.common.by import By
from dataDriven import get_test_data
from time import sleep


@pytest.mark.parametrize("username, password, expected", get_test_data())
def test_login(username, password, expected, setup):
    driver = setup

    driver.find_element(By.ID, "user-name").send_keys(username)
    driver.find_element(By.ID, "password").send_keys(password)
    driver.find_element(By.ID, "login-button").click()

    sleep(1)
    page_source = driver.page_source

    assert expected in page_source, driver.refresh
    driver.back

