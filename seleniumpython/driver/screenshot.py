from selenium import webdriver
import os

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

# driver.save_screenshot(os.getcwd()+"\\jquery.png")
# os.getcwd()----> it will save the screenshot in CURRENT WORKING DIRECTORY(CWD) for that we have to import OS

driver.get_screenshot_as_file(os.getcwd()+"\\jquery1.png")