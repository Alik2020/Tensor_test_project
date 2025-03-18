import pytest
from selenium import webdriver
import logging

logging.basicConfig(level=logging.INFO, filename="tests.log", filemode="a", format="%(asctime)s %(levelname)s %(message)s")

@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(30)
    yield driver
    driver.quit()
