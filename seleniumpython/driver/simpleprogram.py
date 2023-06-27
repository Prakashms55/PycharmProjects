from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")
driver.get("https://www.python.org/")

print(driver.title)
assert "Welcome to Python.org" in driver.title

driver.find_element_by_name("q").send_keys("python")
driver.find_element_by_name("submit").click()

time.sleep(5)
assert "No results found." in driver.page_source