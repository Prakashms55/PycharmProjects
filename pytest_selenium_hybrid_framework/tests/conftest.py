import pytest
from selenium import webdriver

from utilities import configuration


@pytest.fixture()
def setup_and_teardown(request):
    browser=configuration.ReadConfig.launch_browser()
    if browser.__eq__("chrome"):
        driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")
    elif browser.__eq__("edge"):
        driver = webdriver.Edge(executable_path="C:\\Users\\praka\\Documents\\work\\msedgedriver.exe")
    else:
        print("browser is not launched")
    appurl=configuration.ReadConfig.getapplurl()
    driver.get(appurl)
    driver.maximize_window()
    request.cls.driver=driver
    yield
    driver.quit()