#LISTS


# lists are used to store multiple items in a single item
# they are defined with []
# they can be any type ex: int float string in single variable
# lists are immutable
# lists are ordered
# allow dublicate values
list=[12,'sec',3.0,8]
print (list)
# list methods (as these are functions () are complusary)
'''1.append()'''
list.append(8)
print(list)
'''2.clear()'''
#list.clear()
print(list)
'''3.copy'''
x=list.copy()
print(x)
'''4.count()'''
x=list.count(8)
print (x)
'''5.index()'''
print(list.index('sec'))
'''6.insert'''
x=list.insert(1,"1")
print(list)
'''7.pop()'''
list.pop(2)
print(list)
'''8.remove'''
list.remove('1')
print(list)
'''9.reverse'''
x=list.reverse()
print(list)
'''10.sort'''
list=[2,5,6,8,10,4]
list.sort()
print(list)
list=[2,5,6,8,10,4]
list.sort(reverse=True)
print(list)
'''11.extend'''
list.extend([1,2,3])
print(list)