from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")


driver.get("http://google.com")
time.sleep(3)
driver.get("http://python.org")
time.sleep(3)
driver.back()
time.sleep(3)
driver.forward()
time.sleep(3)
driver.refresh()
time.sleep(3)
driver.quit()