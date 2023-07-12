from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")
driver.get("http://python.org")

# ID
# search=driver.find_element_by_id("id-search-field")
# search.send_keys("python")

#NAME
# search_bar=driver.find_element_by_name("q")
# print(search_bar.get_attribute('type'))

# CLASS
# search_button=driver.find_element_by_class_name("python-navigation")
# print(search_button.text)

# TAG NAME
# tag_name=driver.find_elements_by_tag_name("p")
# for i in tag_name:
#     print(i.text)

# LINK TEXT
# link_text=driver.find_element_by_link_text("Learn More")
# print(link_text.text)

# PARTIAL LINK TEXT
# partial_link=driver.find_element_by_partial_link_text("Learn")
# print(partial_link.text)


# MOUSE HOVERING
actions=ActionChains(driver)
downloads=driver.find_element_by_id("downloads")
windows=driver.find_element_by_xpath("//a[text()='Windows'][1]")
actions.move_to_element(downloads).perform()
windows.click()
