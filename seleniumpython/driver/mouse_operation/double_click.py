from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common import keys

driver=webdriver.Chrome(executable_path="C://Users//praka//Documents//work//chromedriver.exe")

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_ev_ondblclick3")

act=ActionChains(driver)

driver.switch_to.frame("iframeResult")

field1=driver.find_element_by_id("field1")
field1.clear()
field1.send_keys("hi buddy!!")

button=driver.find_element_by_xpath("//button[normalize-space()='Copy Text']")
act.double_click(button).perform()
