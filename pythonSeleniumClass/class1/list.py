list=[2,3,4,[5,6],68,0,['m','n'],98,90]
list.extend([100,[899,989]])
print(list.__len__())
print(list.count(2))
print(list.index(0,2,7))
print(list.reverse())
print(list.sort())


# ADDING THE ELEMENTS

list.append(2)
list.extend([100,[899,989]])
list.insert(0,'muthu')
print(list.__len__())

out1=list[1][1]
print(out1)


# REMOVING THE ELEMENTS

list.remove('muthu')
# list.pop(5)
# del list[0]
# del list
# list.clear()



print(list)

