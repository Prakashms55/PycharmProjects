import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("https://seleniumpractise.blogspot.com/2016/08/how-to-handle-autocomplete-feature-in.html")
driver.maximize_window()
orgin=driver.find_element_by_id("tags")

orgin.send_keys("S")
time.sleep(10)
results=driver.find_elements_by_xpath("//li[@class='ui-menu-item']//div")
print(len(results))


for i in results:
    if "BASIC" in i.text:
        i.click()


