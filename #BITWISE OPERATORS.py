# (~) not 
x = 12
print(x)                        # Here the symbol '~' is used as negation,  that means it gives negative number of original value
print(~x)

'''
(simple logic)
x = 2
if we use ~ symbol and print x it will give -3
Because first it will change the x in to neagtive value and add -1 to it

'''

print("___________________\n")

# (&) and 
y = 2 > 3 & 3>2       # Here the & symbol acts as and , if the both statements are correct it returns to true, else it retuns false
print(y)

z = 12 & 13
print(z)

print("___________________\n")

'''
Here in the above problem it returns 12 because:

value of 12 : 00001100
value of 13 : 00001101

According to the truth table
when we use the and(&) operator , if the both staements are 1 then it return 1 , else it return 0

value of 12 : 00001100
value of 13 : 00001101
______________________
output :     00001100
______________________

the value of output is equal to the value of 12 ,  so in the problem it return 12

'''

#(|) or

a =   12 
b =   13
c =   a | b      
print(c)

'''

Here in the above problem it returns 13 because:

value of 12 : 00001100
value of 13 : 00001101

According to the truth table
when we use the OR(|) operator , if any one of the  staements returns 1 then it return 1  , else it return 0

value of 12 : 00001100
value of 13 : 00001101
______________________             
output      : 00001101
______________________

the value of output is equal to the value of 13,  so in the problem it return 13

'''
print("___________________\n")


# (^) XOR

k = 2 ^ 12
print(k)


'''

Here in the above problem it returns 14 beacause

value of 2 : 00000010
value of 12 : 00001100

According to the XOR function:
when the different values(odd values) are present on the both sides it return 1 , else it return 0 

value of 2  : 00000010
value of 12 : 00001100
_______________________
output      : 00001110
_______________________

The value of output is 00001110

|0   |  0   |  0   |  0   |  1   |  1   |  1   |  0    |
|2^7 |  2^6 |  2^5 |  2^4 |  2^3 |  2^2 |  2^1 |  2^0  |

2^3 + 2^2 + 2^1
8 + 4 + 2 = 14

The value of 00001110 is 14
so the it returns 14

'''
print("___________________\n")

f = 1<<2
print(f)      

'''
value of 1 : 00000001
Here when we use the << operator it pushes 2 digits to left hans side

then it becomes = 00000100

|0   |  0   |  0   |  0   |  0   |  1   |  0   |  0    |
|2^7 |  2^6 |  2^5 |  2^4 |  2^3 |  2^2 |  2^1 |  2^0  |

2^2 = 4

The above problems return 4

'''
print("___________________\n")

k = 3 >> 2
print(k)

'''

Similar to above process but it move the digits to right hand side

value of 3 : 00000011
Here when we use the >> operator it pushes 2 digits to right hans side

then it becomes = 0000000

|0   |  0   |  0   |  0   |  0   |  0   |  0   |  0    |
|2^7 |  2^6 |  2^5 |  2^4 |  2^3 |  2^2 |  2^1 |  2^0  |

  
The above problems return 0


'''
print("___________________\n")




