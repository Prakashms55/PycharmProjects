import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")
day="27"
driver.get("https://www.spicejet.com/")
time.sleep(10)
driver.find_element_by_xpath("//div[@data-testid='departure-date-dropdown-label-test-id']").click()

# driver.find_element_by_xpath("//div[@data-testid='undefined-month-July-2023']//div[@data-testid='undefined-calendar-day-"+day+"']").click()
# driver.find_element_by_xpath("//div[@class='css-1dbjc4n r-1loqt21 r-u8s1d r-11xbo3g r-1v2oles r-1otgn73 r-16zfatd r-eafdt9 r-1i6wzkk r-lrvibr r-184en5c']").click()
dates=driver.find_elements_by_xpath("//div[@class='css-1dbjc4n r-k8qxaj']//div[text()='July ']")
for i in dates:
    print(i.text)