from selenium import webdriver
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("https://jqueryui.com/droppable/")

driver.switch_to.frame(0)

src=driver.find_element_by_id("draggable")
target=driver.find_element_by_id("droppable")

actions=ActionChains(driver)
actions.drag_and_drop(src,target).perform()
