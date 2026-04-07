import pytest
from selenium.webdriver import Chrome, ChromeOptions


@pytest.fixture(autouse=True)
def setup():
    o = ChromeOptions()
    o.add_experimental_option('detach', True)
    driver = Chrome(options=o)
    driver.get("https://www.saucedemo.com/")

    yield driver
    driver.quit()
