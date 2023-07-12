from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("https://demoqa.com/alerts")

driver.find_element_by_id("alertButton").click()
alert=driver.switch_to.alert
print(alert.text)
alert.accept()
