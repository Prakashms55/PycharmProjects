set={1,2,34,4,5,'m',1.5}

print(set.__len__())
print(set.__contains__('m'))


# ADDING THE ELEMENTS
set.add('muthu')
set.update({True,55})

# REMOVING THE ELEMENTS
# set.remove('m')
# set.discard('muthu')
# set.clear()
# set.pop()
# del set

print(set)

set1={1,2,3,4}
set2={3,4,5,6}

# UNION
print(set1 | set2)

# INTERSECT
print(set1 & set2)

# INTERMEDIATE DIFFERENCE
print(set1 ^ set2)

# SYSTEMATIC DIFFERENCE
print(set1 - set2)