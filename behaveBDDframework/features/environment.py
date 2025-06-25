from selenium import webdriver
from utilities import configReader

def before_scenario(context,driver):
    browser_name=configReader.Readconfig.launchbrowser()
    if browser_name.__eq__('chrome'):
        context.driver = webdriver.Chrome(executable_path="c:\\Users\\praka\\Documents\\work\\chromedriver.exe")
    elif browser_name.__eq__('edge'):
        context.driver = webdriver.Edge(executable_path="c:\\Users\\praka\\Documents\\work\\msedgedriver.exe")
    else:
        print('browser is not launched')
    context.driver.get(configReader.Readconfig.getapplicationurl())
    context.driver.maximize_window()
def after_scenario(context,driver):
    context.driver.quit()

