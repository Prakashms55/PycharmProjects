"""
type() => The returns the type of the object.
upper() => All the characters in a given string are uppers case.
lower() => All the characters in a given string are lower case.
capitalize() => The first character is the upper case
The title() => The first character in every word of the string is an upper case.
count() => Finds the number of times a specified value in the given string.
find() => Finds the first occurrence of the specified value.
replace() => Replaces a specified phrase with another specified phrase.
isalnum() => Checks whether all the characters in a given string is alphanumeric or not
isalpha() => returns True if all the characters in the string are alphabets
islower() => Checks if all characters in the string are lowercase
isupper() => Checks if all characters in the string are uppercase
strip() => The used to trim whitespaces from the string object
"""

s = "tutor Joes"
print(s)
print(type(s))
print(s.upper())
print(s.lower())
print(s.capitalize())
print(s.title())
print(s.count("t"))
print(s.endswith("ED"))
print(s.find("o"))
print(s.find("o", 5))
print(s.replace("o", '0'))

a = "joes1234"
print("Is Upper : ", a.isupper())
print("Is Lower : ", a.islower())
print("Is Alpha Numeric : ", a.isalnum())
print("Is Alpha : ", a.isalpha())

s = "he\nis\ngood"
print(s)
print(s.splitlines())
print(s.splitlines(True))

a = "Tutor Joes Computer Education"
print(a.split(" "))
a = "Tutor,Joes,Computer,Education"
print(a.split(","))

s="    Joes     "
print(len(s))
print(len(s.strip()))
print(len(s.lstrip()))
print(len(s.rstrip()))

s='12-03-2020'
print(s.partition('-'))
