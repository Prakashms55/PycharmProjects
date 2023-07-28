from selenium import webdriver
def chrome_headless():
        ops=webdriver.ChromeOptions()
        ops.headless
        driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe",options=ops)
        return driver
driver=chrome_headless()
print(driver.title)
print(driver.current_url)
      # it will give the result without launching browser
      # -------------------IT'S NOT WORKING----------------------------

