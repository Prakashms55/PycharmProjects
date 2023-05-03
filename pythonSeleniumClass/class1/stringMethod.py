########################################################################################################################

# capitalize :
#                 In Python, the capitalize() method converts first character of a string to uppercase letter and
#                 lowercases all other characters, if any.
# string.capitalize()
# input  : The capitalize()function doesn't take any parameter.
# return : The capitalize() function returns a string with the first letter capitalized and all other characters
#          lowercased. It doesn't modify the original string.
# Note   : It doesn't modify the original string.

########################################################################################################################
# Example of string capitalized method
# s = "pyThON"
# print(s)                                           # pyThON
# print(id(s))                                       # 1755651263856
# output = s.capitalize()
# print(output)                                      # Python
# print(id(output))                                  # 1755651288176
# print(s)                                           # pyThON
# print(id(s))                                       # 1755651263856

########################################################################################################################
# title : The title() method returns a string with first letter of each word capitalized; a title cased string.
# str.title()
# Input  : title() method doesn't take any parameters.
# return : title() method returns a title cased version of the string. Meaning, the first character of each word is
#          capitalized (if the first character is a letter).
# Note :   It doesn't modify the original string.

########################################################################################################################
# # Example of How Python title() works?
# text = 'My favorite number is 25.'
# title_output = text.title()
# print(title_output)                                          # My Favorite Number Is 25.
# print(text)                                                  # My favorite number is 25.
#
# text = '234 k3l2 *43 fun'
# title_output = text.title()
# print(title_output)                                          # 234 K3L2 *43 Fun
# print(text)                                                  # 234 k3L2 *43 fun
#
# # Example of title() with apostrophes
# text = "He's an engineer, isn't he?"
# title_output = text.title()
# print(title_output)                                          # He'S An Engineer, Isn'T He?
#
# # Note : title() capitalizes the first letter after apostrophes as well as shown in above example.
# #        To solve this issue, you can use regex in python.
##########################################################################################
##########################################################################################

#center() The center() --> returns a string which is padded with the specififed charcter.
# string.center(width, fillchar)

# s="python"
# out=s.center(9,"*")
# print(out)
# s="python"
# out=s.center(9)
# print(out)
# print(len(s))
##########################################################################################
##########################################################################################

#count():- count() --->searches the substring in the given string and return how  many times substring present in it .
# string_out="python is awesome programing language"
# sub_string="is awesome"
# out=string_out.count(sub_string)  # it will give pos int to count the substring , is substring does not exist then it will return 0
# print(out)

# string_input= 'python is awesome is , programing is lang is'
# sub_string='is'
# out=string_input.count(sub_string,6,20)#  string.count(substring, start, end )it will give pos int to count the substring , is substring does not exist then it will return 0
# print(out)

# s = " "
# print(type(s))
# print(s)
# print(id(s))
# print(len(s))
##########################################################################################
##########################################################################################

# func --> method --> performaing operation --> returning -->

#startwith()
# s="python is good programing language"
# s1="python"
# out=s.startswith(s1) #return boolean type(true/false)
# print(out)

#endswith
# s="python is good programing language"
# out="language"
# print(s.endswith(out)) #return boolean type(true/false)
##########################################################################################
##########################################################################################

#find()
# s="Let it be,let it be ,let it be"
# print(s.find("let it be")) # return the index where substring is exist

# s="Let it be,let it be ,let it be"
# print(s.find("python"))  # return the index , -1 substring is not exist in main string
##########################################################################################
##########################################################################################

#strip -----> it will remove only the starting and ending characters or string
# s="  redmi is good phone  "
# print(s.strip())

# s="redmi is good phone"
# out=s.strip("re") # it will remove the starting letter of re in redmi
# print(out)
#
# string = 'android is android'
# strip_out = string.strip('id')  # it will remove the ending letter of id in android
# print(strip_out)
##########################################################################################
##########################################################################################

#split() ------> it will split individual sentence in the list datatype
# s="android is good"
# out=s.split()
# print(out)
##########################################################################################
##########################################################################################

#islow()
# s="android is good"
# out=s.islower()
# print(out)

# s="Android is Good"
# out=s.islower()
# print(out)
##########################################################################################
##########################################################################################

#isupp()
# s="ANDROID IS GOOD"
# out=s.isupper()
# print(out)

# s="ANDROID is GoOD"
# out=s.isupper()
# print(out)

##########################################################################################
##########################################################################################

#alnum()
# s="1234ABCD"
# out=s.isalnum()
# print(out)

# s="12345"
# print(s.isalnum())
#######################################################################################
#alpha()
# s="ABCD"
# print(s.isalpha())

# s="abcd"
# print(s.isalpha())
#######################################################################################

#isdigit()
# s="12345"
# print(s.isdigit())

# s="Abcd1234"
# print(s.isdigit())
########################################################################################

#isdecimal()
# s="1234"
# print(s.isdecimal())