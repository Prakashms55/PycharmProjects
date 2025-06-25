

import allure
import pytest
from allure_commons.types import AttachmentType
from selenium import webdriver

from utilities import configuration

@pytest.fixture()
def log_on_failure(request):
    yield
    item = request.node
    if item.rep_call.failed:
        allure.attach(driver.get_screenshot_as_png(), name="failed_test",
                      attachment_type=AttachmentType.PNG)


@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)
    return rep

@pytest.fixture()
def setup_and_teardown(request):
    browser=configuration.ReadConfig.launch_browser()
    global driver
    driver=None
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

