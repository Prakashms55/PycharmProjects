from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("https://jqueryui.com/datepicker/")

driver.switch_to.frame(0)
# Approach 1
# driver.find_element_by_id("datepicker").send_keys("07/13/2023")

# Approach 2
mon="May"
yr="2024"
day="24"
driver.find_element_by_id("datepicker").click()

while True:
    month = driver.find_element_by_xpath("//span[@class='ui-datepicker-month']").text
    year = driver.find_element_by_xpath("//span[@class='ui-datepicker-year']").text
    if mon==month and yr==year:
        break
    else:
        driver.find_element_by_xpath("//a[@data-handler='next']/span").click()
# select date
dates=driver.find_elements_by_xpath("//div[@id='ui-datepicker-div']//table//tr//td//a")
for date in dates:
    if day==date.text:
        date.click()
        break
