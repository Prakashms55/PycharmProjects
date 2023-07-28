from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

# driver.get("https://demo.nopcommerce.com/")
# driver.maximize_window()
# # it opens a new tab for the register we click
# driver.find_element_by_xpath("//a[normalize-space()='Register']").send_keys(Keys.CONTROL+Keys.ENTER)
# for window in driver.window_handles:
#     driver.switch_to.window(window)
#     if driver.title.__eq__("nopCommerce demo store. Register"):
#         print("page is loaded correctly")
#         fn=driver.find_element_by_id("FirstName").is_displayed()
#         print(fn)

# IN SELENIUM 4 ---> WE CAN OPEN A NEW TAB
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.newwindow("tab")
# driver.get("https://google.com/")
#
# # IN SELENIUM 4 ---> WE CAN OPEN A NEW window
# driver.get("https://demo.nopcommerce.com/")
# driver.switch_to.newwindow("window")
# driver.get("https://google.com/")