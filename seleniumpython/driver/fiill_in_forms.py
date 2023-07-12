from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("https://demo.automationtesting.in/Register.html")
driver.maximize_window()

fname=driver.find_element_by_xpath("//input[@placeholder='First Name']")
fname.send_keys("vijay")

lname=driver.find_element_by_xpath("//input[@placeholder='Last Name']")
lname.send_keys("kumar")

email=driver.find_element_by_xpath("//input[@type='email']")
email.send_keys("test123@gmail.com")

driver.close()