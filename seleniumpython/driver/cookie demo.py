from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")
driver.get("http://example.com")
# Adding cookies to the current session
cookie={'name':'vijay','name2':'kumar'}
driver.add_cookie(cookie)
# getting the single cookie
print(driver.get_cookie('name'))
# getting all the cookies in the session
print(driver.get_cookies())
# deleting the particular cookie
driver.delete_cookie('name')
# deleting all the cookies
driver.delete_all_cookies()