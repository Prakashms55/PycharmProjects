from selenium import webdriver
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# # it will run the code in different systems by using below steps
#
# # driver=webdriver.Remote(
# #                 command_executor='http://33.33.33.1:4444/wd/hub',
# #                 desired_capabilities=DesiredCapabilities.CHROME
# # )
# #
# # driver.get("")
#
# x=10
# y=10
# print(type(x))
# print(type(y))
# print(id(x))
# print(id(y))
driver = webdriver.Edge(executable_path="c:\\Users\\praka\\Documents\\work\\msedgedriver.exe")
driver.get("https://tutorialsninja.com/demo/")
driver.find_element_by_name("search")
driver.find_element_by_xpath("//button[@class='btn btn-default btn-lg']").click()
msg=driver.find_element_by_xpath("//div[@id='content']//p[2]").text
print(msg)