from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("https://admin:admin@the-internet.herokuapp.com//basic_auth")
 # Syntax:("https://username:password@the-internet.herokuapp.com//basic_auth")
