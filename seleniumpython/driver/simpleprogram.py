from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")
driver.get("https://www.python.org/")

print(driver.title)

driver.find_element_by_name("q").send_keys("python")
driver.find_element_by_name("submit").click()

page=driver.page_source
assert "No results found." not in page