from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")
driver.get("https://google.com//")

search=driver.find_element_by_name('q')
act=ActionChains(driver)

act.key_down(Keys.SHIFT)
act.send_keys_to_element(search,'python')
act.key_up(Keys.SHIFT)
act.send_keys(Keys.ENTER)
act.perform()