a = 3
b = 6

#method-1

temp = a
a  = b
b = temp
print(a)
print(b)

#method-2

c = 9
d = 2
c,d = d,c
print(c)
print(d)

#method-3
p = 8
q = 5
p += q
q =  p - q
p = p - q

print(p)
print(q)

#method-3
p = 8
q = 5
p ^= q                     # ^ = XOR
q =  p ^ q
p = p ^ q

print(p)
print(q)

