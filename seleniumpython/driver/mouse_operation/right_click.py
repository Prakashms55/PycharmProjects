from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C://Users//praka//Documents//work//chromedriver.exe")

driver.get("https://swisnl.github.io/jQuery-contextMenu/3.x/demo.html")

right_click=driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")
act=ActionChains(driver)
act.context_click(right_click).perform()

value=driver.find_element_by_xpath("//span[normalize-space()='Copy']").click()
driver.switch_to.alert.accept()
