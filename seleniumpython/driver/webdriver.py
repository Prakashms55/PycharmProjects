from selenium import webdriver
chromedriver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")
# edgedriver=webdriver.Edge(executable_path="C:\\Users\\praka\\Documents\\work\\msedgedriver.exe")

chromedriver.get("https://mail.google.com/")
# edgedriver.get("https://www.amazon.in/")