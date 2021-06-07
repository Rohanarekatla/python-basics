'''
Varaibles can store the data in different types

Types:
1.Text type
2.Numeric type
3.sequence type
4.Mapping type
5.set types
5.Boolean types

'''

'''
Text type :
1.string
'''

#string

x = 'Thomas shelbey'
print(x)
print(type(x))

#convertion in to strings
#syntax = str(iteams)

y = str(2)
print(y)
print(type(y))                #by using this str function we can convert any thing in to string

'''
Numeric datatypes:
1.int
2.float
3.complex

'''

#int

a = 1
print(a)
print(type(a))

#conversion in to integers
#syntax = int(iteam)

b = int(23.0)
print(b)
print(type(b))

#float

p = 1.2
print(p)
print(type(p))

#conversion in to floats
#syntax = float(iteam)

q = float(1)
print(q)
print(type(q))


#complex

c = 3j
print(c)
print(type(c))

#convesion in to complex

c =complex(3)
print(c)
print(type(c))

#conversion of  two numbers in complex

d = 5
e = complex(c,d)
print(e)
print(type(e))

'''
sequence types:
1.List
2.tuple
3.range

'''

#List

lst = [1,2,3,4,5]
print(lst)
print(type(lst))

#conersion in to list
#syntax = list((iteams))

lst_1 = list((1,3,2,8,5))
print(lst_1)
print(type(lst_1))

#tuple

tuple_1 = (2,5,3,6)
print(tuple_1)
print(type(tuple_1))

#conversion in to tuple

tuple_2 = tuple([1,3,6,8,9])
print(tuple_2)
print(type(tuple_2))

#range
num = range(5)
print(num)
print(type(num))

'''
Mapping type:
dict

'''
#dict

dict_1 = {'Nikhil':2003,"rohan" : 2002,"nag" :2003 }
print(dict_1)
print(type(dict_1))


'''
set types
1.set
2.frozen set

'''

#set

set_1 = {1,2,3}
print(set_1)
print(type(set_1))

#conversion in set

set_2 = set([1,2,3,4,5])
print(set_2)
print(type(set_2))

#frozen set

fz_1 = frozenset({1,2,3,4})
print(fz_1)
print(type(fz_1))

#conversion in to frozen set

fz_2 = frozenset((1,2,3))
print(fz_2)
print(type(fz_2))

'''
Boolean type:
1.bool
'''

#bool

w = 2>1
print(w)
print(type(w))

#conversion in to booleans

z = bool(0) 
m = bool(1)
print(z)
print(m)
print(type(z))
print(type(m))
