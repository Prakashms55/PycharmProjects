from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("http://amazon.com")

driver.find_element_by_id("twotabsearchtextbox").send_keys("python book")

driver.find_element_by_id("nav-search-submit-button").click()

suggestions=driver.find_elements_by_xpath("//a[@class='a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal']//span")
print(len(suggestions))
for suggestion in suggestions:
    print(suggestion.text)
    if 'Computer Science and Data Science' in suggestion.text:
        suggestion.click()
    # if 'python book' in suggestion.text.lower():
    #     suggestion.click()
    #     break