'''
String :- a string is a seq of characters enclosed within a single or double quotation.


'''

# string_name = 'python'  # "python" ''''
# string_name_01 = '''python
#               classes'''

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

# out = x1[0:2]
# print(out)
# out1 = x1[2:5]
# print(out1)
# out2 = x1[:]
#
# print(out2)
# out3 = x1[:5]
# print(out3)

#out=x1[-1:-4:-1]
#print(out)

# string concatenation
# s1="python"  # we cant add string + int (or any data type) if you add then it throw--->type error
# s2="program" # we must add string + string
# print(s1+" "+s2)

# string repetition----->(no of times * <String value>)
# s="python "
# s1=5*s # it will execute for 5 times
# print(s1)

# string membership----->(in / not in)===>it will give result in boolean type(True/False)
#s="python is a good programing language"
# s1="python" in s
# print(s1) #---->(True)
# s2="java" in s
# print(s2)
# s3="a" in s
# print(s3)
# s4="Python" not in s # Python----> 1st letter of Python is capital letter but it in s=python it is in small letter
# print(s4)

# string is iterable
# x="python" # input data----> p,y,t,h,o,n ==>for loop
# for i in x:
#     print(i)
