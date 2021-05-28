#NUMPY
'''
NUMPY are faster than lists because of less usage of memory
'''
'''applications of Numpy
    1.mathematics
    2.matplotliv
    3.backend(pandas,coonect 4,digital Photography)
    4.machine learning'''


'''load in numpy'''
import numpy as np

a=np.array([1,2,3])#one demensional array
print(a)
b=np.array([[9.0,8.0,6.0],[6.0,5.0,4.0]])#two demensional array
print(b)
#get Dimensions
print(a.ndim)
#get shape
print(b.shape)
#get type
print(a.dtype)
#to specify which type 
a=np.array([1,2,3],dtype='float')
print(a.dtype)
#get size
print(a.itemsize)
#get total size
print(a.size)
print(a.nbytes)
#Accessing/changing specific elements,rows ,columns
a=np.array([[1,2,3,4,5,10],[6,7,8,9,11,12]])
print(a)
print(a.shape)
#get specific element notation[r,c]
print(a[1,-3])
#get specific row
print(a[0,:])
#get specific column
print(a[:,4])
#getting little more fancy [start(index):end(index):stepsize]
print(a[1,1:6:2])
#change element
a[1,5]=38
print(a)
a[:,2]=5
print(a)
#3D example
c=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(c)
#get specific element(work outside in)
print(c[:,1,:])
#replace 
c[:,1,:]=[[9,9],[9,9]]
print(c)
'''Initializing differnet types of array'''
#all 0s matrix
print(np.zeros(5))
print(np.zeros((3,3,2)))#(number of matrix,rows,colowns)
#all 1s in matrix
print(np.ones((2,3,3), dtype='int32'))#(number of matrix,rows,colowns)
#fill with any other number
print(np.full((2,3,3),10))
#any other number(full_line)
print(np.full_like(a,4))#print like matrix a
#random decimal numbers
print(np.random.rand(4,4))
#random int values
print(np.random.randint(100,size=(3,3)))
#the identity matrix
print(np.identity(5))
'''Be careful when copying arrays'''
a=np.array([1,2,3])
b=a
b[0]=100
print(a)
print(b)
#change in a will reflect values  in b
a=np.array([1,2,3])
b=a.copy()
b[0]=100
print(a)
print(b)
'''Maths'''
a=np.array([1,2,3])
print(a)
print(a+2)#+-/* are possible
print(a+b)#shape should be same
print(a**2)
#sin cos tan etc are also possible
'''linear algebra'''
# if we use matmul even if the shapes are differnet we can use maths
print(np.matmul(a,b))
#Find the determinant
c=np.identity(6)
print(np.linalg.det(c))
''' we can find det trace vector decomp,eigen values,inverse etc'''
'''Statics'''
#min,max
#reshape
#a=b.reshape((2,2))
#vertically stacking vectors
#print(np.vstack[a,b])
#horizontal stacking
#print(np.hstack([a,b]))




