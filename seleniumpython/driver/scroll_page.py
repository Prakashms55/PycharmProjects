import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C://Users//praka//Documents//work//chromedriver.exe")

driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")

# scroll into particular point
# driver.execute_script("window.scrollBy(0,3000)"," ")
# value=driver.execute_script("return window.pageYOffset;")
# print("no of pixels moved : ",value)

# scroll in to particular element
# flag=driver.find_element_by_xpath("//img[@alt='Flag of India']")
# driver.execute_script("arguments[0].scrollIntoView();",flag)
# value=driver.execute_script("return window.pageYOffset;")
# print("no of pixels moved : ", value)

# scroll into page upward and downward
# downward
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("no of pixels moved : ", value)

time.sleep(3)

# upward
driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
value=driver.execute_script("return window.pageYOffset;")
print("no of pixels moved : ", value)