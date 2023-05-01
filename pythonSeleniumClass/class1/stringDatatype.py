'''
String :- a string is a seq of characters enclosed within a single or double quotation.


'''

string_name = 'python'  # "python" ''''
string_name_01 = '''python
              classes'''

# s = "programming"
# x = 100
# s1 = x
# print(type(s)) ---->it defines what type of data it is
#
# print(id(s))------> it defines the memory location


# string slicing

s = 'python'

'''
     P    Y      T    H    O    N
     0    1      2    3    3    5
    -6    -5    -4    -3   -2   -1

    hon
    3 : end 
    1:  t postion 


s[start:stop-1:step] 


'''

x1 = 'Python'

# s[start:stop-1:step]  # py
out = x1[0:2]
print(out)
out1 = x1[2:5]
print(out1)
out2 = x1[:]

print(out2)
out3 = x1[:5]
print(out3)