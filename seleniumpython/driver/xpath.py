from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("http://ebay.com")

driver.find_element_by_id("gh-ac").send_keys("python book")

driver.find_element_by_id("gh-btn").click()

suggestions=driver.find_elements_by_xpath("//div[@class='s-item__title']")

for suggestion in suggestions:
    if 'python book' in suggestion.text.lower():
        suggestion.click()
        break