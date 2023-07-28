from selenium import webdriver
import time

from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")
driver.get("https://www.python.org/")

print(driver.title)
assert "Welcome to Python.org" in driver.title

act=ActionChains(driver)

# driver.find_element_by_name("q").send_keys("python")
# driver.find_element_by_name("submit").click()

search=driver.find_element_by_name("q")
# act.key_down(Keys.SHIFT)
act.send_keys_to_element(search,"python")
act.send_keys(Keys.ENTER)
act.perform()


# time.sleep(5)
# assert "No results found." in driver.page_source