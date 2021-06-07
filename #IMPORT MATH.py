import math

#for using the math functions in python we need import them first
'''
we can also use only the specefic math functions by :

from math import sqrt,pow
'''

'''
1.pow()
2.abs()
3.floor()
4.ceil()
5.pi()
6.max()
7.min()

'''


x = pow(2,3)
print(x)                             #return the value of 2 power 3
print("___________________\n")

print(math.floor(2.5))               #return the floor value(preceeding) of 2.5(simple mark : floor means down so it return preceeding value)
print("___________________\n")

print(math.ceil(2.5))                #return the ceil value (succeding) of 2.5 (simple mark : ceil means up (ceiling) so it return succeding value )
print("___________________\n")

a = math.pi
print(a)                             #return the exact value of pi
print("___________________\n")


print(min(3,4,5,8))                  #return the minimum value (least value)
print("___________________\n")

print(max(2,4,7,9))                  #return the maximum value (greater value)
print("___________________\n")


print(abs(-2.55))                   # retun absolute (positive) value of the number


