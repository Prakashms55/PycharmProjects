from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C://Users//praka//Documents//work//chromedriver.exe")

driver.get("https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/")

src1=driver.find_element_by_xpath("(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[1]")
print(src1.location)   #{'x': 59, 'y': 250}
src2=driver.find_element_by_xpath("(//span[@class='ui-slider-handle ui-corner-all ui-state-default'])[2]")
print(src2.location) #{'x': 412, 'y': 250}

act=ActionChains(driver)

act.drag_and_drop_by_offset(src1,59,0).perform()
print(src1.location)
act.drag_and_drop_by_offset(src2,100,0).perform()
print(src2.location)