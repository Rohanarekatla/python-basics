'''
sets are used to store the iteams in the single varaible
Propeties:
1.immutable(Unchangeable)
2.unordered
3.Not allow duplicate values

'''
set_1 = {"Nikhil" , 9 ,True ,3.5}   #we can acess integers, float values , strings , boolean values
print(set_1)
print(type(set_1))


#We cannot access or change the list iteams (because they are un-ordered and un changeable)

'''

Sets methods:
1.add
2.clear
3.copy
4.diffeence
5.difference update
6.discard
7.intersection
8.intersection update
9.isdisjoint
10.issuperset
11.pop
12.issubset
13.remove
14.symmentric difference
15.symmentric difference update
16.union
17.update

'''
"1."#add()
#syntax = varaible.add(iteam)

set_1.add("Thomas_shelbey")          # we can add integers.float values,boolean values ,strings
print(set_1)

"2."#clear()
#syntax = varaible.clear()

set_2 ={1,2,3,4,5,6,7}
set_2.clear()                       #clear all the iteams in the set
print(set_2)

"3."#copy()
#syntax= New_List = variable.copy()

set_3 = set_1.copy()
print(set_3)                      # copy all the iteams in to the new set

"4."#difference()
#syntax =  New_varaible = normal set.difference(comparing set)

set_4 = {"Thomas_shelbey","Aurthur_shelbey","jhon_shelbey"}
set_5 = set_4.difference(set_1)          #remove the similar iteam of both sets(set_4 and set_1) , in set_4 and print the remaining iteam in the set_4
print(set_5)

"5."#difference_update()
#syntax = normal set.difference(comparing set)

set_4.difference_update(set_1)           #It removes similar iteams directly from the original set no need to create new set
print(set_4)

"6."#discard()
#syntax = varaible.discard(iteam)

set_6 = {99,33,34,2,356,121}           # it removes the specefic value from the set bit different fron remove
set_6.discard(1)                       # it could not makes an error if the value is not even present in the set
print(set_6)

"7."#intersection()
#syntax = New_varabile = set1.intesection(set2)

set_7 = {99,121,5,7,8,0}
similar = set_6.intersection(set_7)    # return the similar iteams in  both sets
print(similar)

"8."#intesection_update()
#syntax = set1.intesection_update(set2)

set_6.intersection_update(set_7)        #It removes similar iteams directly from the original set no need to create new set
print(set_6)

"9."#isdisjoint()
#syntax = New_varaibe = set1.isdisjoint(set_2)

similarity = set_6.isdisjoint(set_7)    #if there is no similar iteam in the both sets it returns True else it return False
print(similarity)

"10."#issuperset()
#syntax = New_varaibe = set1.isdisjoint(set_2)

set_8 = {1,2,3}
set_9 = {1,2,3,4,5,6}
set_10 = set_9.issuperset(set_8)        # it return True if all the elements in the set1 present in set2 ,else False
print(set_10)


"11."#pop()
#syntax = varaible.pop(index)

set_9.pop()                             # It removes random iteam from the set
print(set_9)                           

"12."#issubset()
#same as issuperset() function

"13."#remove()
#syntax = varaible.remove(iteam)

set_8.remove(3)
print(set_8)                           #Remove the specefic iteam from the list

"15."#symmentric_difference()
#syntax = New_varaibe = set1.symmenteric_difference(set_2)

Final = set_8.symmetric_difference(set_9)
print(Final)                           #It remove all the similar iteams from both sets and return remaining iteams of both sets

"16."#symmentric_difference_update()
#syntax = set1.symmenteric_difference(set_2)


set_8.symmetric_difference_update(set_9)  
print(set_8)                              #It removes similar iteams directly from the original set and return all the remaining values in the original set


"17."#union()
#syntax = New_vaaible = set1.union(set2)

set_11 = {1,2,3}
set_12 = {3,4,5}
                                          
N = set_11.union(set_12)                  # It return all the iteams in the both the sets , and it could not repeat the values
print(N)

"18."#update()
#syntax = set1.update(set2)   

set_11.update(set_12)
print(set_11)                             # return all the iteams in the both sets in to the original set (no need create new varabile)
