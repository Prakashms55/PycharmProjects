from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:\\Users\\praka\\Documents\\work\\chromedriver.exe")

driver.get("https://testautomationpractice.blogspot.com/")

# 1.count no of rows
no_of_rows=driver.find_elements_by_xpath("//table[@name='BookTable']//tr")
print(len(no_of_rows))
#
# # count no of column
no_of_columns=driver.find_elements_by_xpath("//table[@name='BookTable']//th")
print(len(no_of_columns))

# 2.read specific row and column
# data=driver.find_element_by_xpath("//table[@name='BookTable']//tr[2]/td[3]").text
# print(data)

# 3.read all the rows and column data
# for row in range(2,len(no_of_rows)+1):
#     for col in range(1,len(no_of_columns)+1):
#         data=driver.find_element_by_xpath("//table[@name='BookTable']//tr["+str(row)+"]/td["+str(col)+"]").text
#         print(data,end="                          ")
#     print()

# 4.read data based on condition
# for row in range(2,len(no_of_rows)+1):
#     author_name=driver.find_element_by_xpath("//table[@name='BookTable']//tr["+str(row)+"]//td[2]").text
#     # print(author_name)
#     if author_name=="Mukesh":
#         datas=driver.find_elements_by_xpath("//table[@name='BookTable']//tr["+str(row)+"]//td")
#         # print(datas,"    ",author_name)
#         for data in datas:
#             print(data.text,end="  ")
#         print()