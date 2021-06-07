'''
Dictionaries are used to store the values in key : value pairs
properties:
1.ordered
2.immutable
3.Not allow duplicate values

'''

dict_1 = {

    "Nikhil" : 18,
    "Rohan" : 18,            #syntax {key : value}
    "Mani" : 18              #we can use integers , float values ,strings , boolean values
}
print(dict_1)
print(type(dict_1))

#acessing dictionaries
dict_2 = {
    "Peaky_blinders" : ["Thomas_shelbey","Aurthur_shelbey","Jhon_shelbey"],
    "Peaky" : {"Grace" :"wife of thomas shelbey",
               "Linda" : "Wife of aurthur shelbey",
               "Eseme" : "Wife of jhon shelbey",
               "Polly gray" : "Family member of peaky blinders"
               }
}
print(dict_2["Peaky"]["Eseme"])

#converting lists in to dictionaries

Keys = ["Thomas_shelbey","Aurthur_shelbey","Jhon_shelbey"]
Values = ["Grace","Linda","Eseme"]
data = dict(zip(Keys,Values))
print(data)

#changing the dictonaries

data["Thomas_shelbey"] = "Lizzie"
print(data)

#adding new iteams to the dictonaries

data["Freddie_Throne"] = "Ada_shelbey"
print(data)

'''
Dictionary methods:
1.clear
2.copy
3.from keys
4.get
5.iteams
6.keys
7.pop
8.pop iteam
9.set default
10.update
11.values

'''

"1."#clear()
#syntax = varaible.clear()

dict_3 = {
    1 : "Thomas_shelbey",
    2: "Ragnar_Lothbork",      #clear all the iteams in the dictionary
    3: "Alfie_solomons"
}
dict_3.clear()
print(dict_3)

"2."#copy
#syntax = varaible.copy()

dict_4 = dict_1.copy()       #copy all the iteams in to the new dictionary
print(dict_4)

"3."#fromkeys()
#syntax = New_varaible =  dict.fronkeys(keys,values)

names = ("Naga pranay","sushnath","Rohan","Pradeep","Giri","mani","ashish","surya")
age = 18
dict_5 = dict.fromkeys(names,age) 
print(dict_5)

"4."#get()
#syntax = New_varaible = varaible.get()

acess = dict_5.get("Rohan")
print(acess)               # return the of specefic key value


"5."#iteams()
#syntax = New_varaible = varaible.iteams()

Total = dict_5.items()    #return all the iteams in the dictionaries
print(Total)

"6."#keys
#syntax = New_varaible = varaible.keys()

Keys_iteams = dict_5.keys()
print(Keys_iteams)        # return all the key iteams in the dictionary

"7."#pop
#syntax = varaible.pop(key)

dict_5.pop("ashish")
print(dict_5)             #remove the iteam with specefic key value

"8."#pop iteam
#syntax =varaible.popiteam()

dict_4.popitem()          #remove the last iteam of the dictionary
print(dict_4)

"9."#setdefault()
#syntax = New_varaible = varaible.setdefault()

new = dict_4.setdefault("Mani",19)
print(new)
print(dict_4)              #return the value of the given key if ot exists in the dictionary ,else add the given key and value to the dictionary

"10."#update
#syntax = varaible.update()

dict_4.update({'Naga pranay' : 18})
print(dict_4)              #insert the key and value in to the dictionary

"11."#values
#syntax = New_varaible = varaible.values()

age_p = dict_4.values()
print(age_p)               #return the values of the dictionary

