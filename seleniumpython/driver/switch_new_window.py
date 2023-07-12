from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("http://python.org")

driver.execute_script("window.open('');")

driver.switch_to.window(driver.window_handles[1])
driver.get("http://google.com")