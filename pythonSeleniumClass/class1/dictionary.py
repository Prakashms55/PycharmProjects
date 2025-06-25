dict={1:5,2.0:'m',3:"muthu",4:55}

# INSERT THE ELEMENTS

# insertion
dict[100]=200

# set default
dict.setdefault(55,555)

# update
dict.update({'name':"prakash"})

# REMOVING THE ELEMENTS
# dict.clear()
dict.pop(4)
# dict.popitem()
# del dict


print(dict.get('name'))
print(dict[100])
print(dict.get(200,1989))



print(dict)