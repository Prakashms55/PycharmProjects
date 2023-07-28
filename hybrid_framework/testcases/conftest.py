import pytest
from selenium import webdriver
@pytest.fixture()
def setup():
        driver=webdriver.Chrome(executable_path="\\Users\\praka\\Documents\\work\\chromedriver.exe")
        return driver
