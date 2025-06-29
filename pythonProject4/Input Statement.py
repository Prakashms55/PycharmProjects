"""
name = input("Enter the Name : ")
print(name)
print(type(name))

#----------------------------------------------------------------

a= int(input(" Enter the value of A : "))
b= int(input(" Enter the value of B : "))
c=(a+b)

print(c)
print(type(c))
#-------------------------------------------------------------------

a= float(input(" Enter the value of A : "))
b= float(input(" Enter the value of B : "))
c=(a+b)

print(c)
print(type(c))



name1,name2,name3=("Muthu","prakash","Saktivel")

print(name2)

detail=name4,age,date_of_birth=input("Enter the Details : ").split(',')
print(detail)
print(age)



# MultiLine String

a="""
# This is the most common and recommended way to create multi-line comments,
# especially for documentation purposes (known as docstrings).
# You enclose the text of your comment within three single quotes or three double quotes
"""
print(type(a))
print(a)

"""

# String Paragrap

para=[]
print("Enter the para : ")

while True:
    line=input()
    if line:
        para.append(line)
    else:
        break
    print(para)
    output= '\n'.join(para)
    print(output)