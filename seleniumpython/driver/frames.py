from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("https://demoqa.com/frames")

driver.switch_to.frame("frame1")

txt=driver.find_element_by_id("sampleHeading").text
print(txt)

driver.switch_to.default_content()
driver.switch_to.frame("frame2")

txt1=driver.find_element_by_id("sampleHeading").text
print(txt1)