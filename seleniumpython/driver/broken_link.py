import requests
from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("http://www.deadlinkcity.com/")

links=driver.find_elements_by_tag_name("a")
print(len(links))
count=0
valid=0

for i in links:
    url=i.get_attribute("href")
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url," is broken link")
        count+=1
    else:
        print(url," is valid link")
        valid+=1
print("broken link : ",count)
print("valid link : ",valid)