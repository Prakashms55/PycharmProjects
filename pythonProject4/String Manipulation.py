"""
  s [ start : end ]
   s [ start : ]
   s [ : end ]
   s [ : : ]

This program is using the concept of slicing in python, which allows you to extract a portion of a string by specifying a range of indices.

The following operations are performed in the above code:

print(s): This line will print the original string "sample".
print(s[0:2]): This line uses slicing to extract a substring of the original string "sa", starting at index 0 and ending at index 2 (not included).
print(s[:5]): This line uses slicing to extract a substring of the original string "sampl", starting at index 0 and ending at index 5 (not included).
print(s[1:]): This line uses slicing to extract a substring of the original string "ample", starting at index 1 and going till the end of the string.
print(s[-1]): This line uses slicing to extract the last character of the string "e" by specifying the index as -1, as in python, negative index is used to access elements from the end of the list.
print(s[-2:-1]): This line uses slicing to extract the second last character of the string "l" by specifying the range as -2 to -1, as in python
"""

# String Manipulation
'''
 S  a  m  p  l  e
 0  1  2  3  4  5
-6 -5 -4 -3 -2 -1
'''

s = "sample"
print(s)
print(s[0:2])
print(s[:5])
print(s[1:])
print(s[-1])
print(s[-2:-1])
print(s[:-1])
print(s[::-1])