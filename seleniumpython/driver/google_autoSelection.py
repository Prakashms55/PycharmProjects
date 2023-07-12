import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("https://google.com")
driver.maximize_window()
time.sleep(20)
driver.find_element_by_id("APjFqb").send_keys("python selenium")

results=driver.find_elements_by_xpath("//div[@id='sBQTL']//div[1]")
print(len(results))

for i in results:
    print(i.text)