'''

Tuples are used  to store the multiple iteams in a single varaible
Properties:
1.unmutable(Unchangeable)
2.orderd
3.Allow duplicate values

'''




Tuple_1 = ("Nikhil" , 9 ,True ,3.5)   #we can acess integers, float values , strings , boolean values
print(Tuple_1)
print(type(Tuple_1))

#Acessing the Tuple iteams 
#1
print(Tuple_1[1])  # print the first index iteam in the Tuple

#2
print(Tuple_1[0:3]) # printing te first 3 iteams in the Tuple, It take up to 3 so it would not print 3rd  value 

# we cannot change the tuple iteams because tuples are immutable

'''

Tuple methods :
1.count
2.index


''' 
"1."#count()
#syntax = varaible.count(iteam)

Tuple_2 = (1,2,3,3,3,3,3,3)
count = Tuple_2.count(3)            #show the the count of the given iteam in the Tuple
print(count)

"2."#index()
#syntax = varaible.index(iteam)

position = Tuple_1.index("Nikhil")   #Give you the index value
print(position)       



