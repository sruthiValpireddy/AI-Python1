#Lists are the collection of items which are ordered and changeable. They allow duplicate members.

listofitems=["apple","banana","grapes","mango"]
listofnums=[1,2,3,4,5,6,7,8,9]
listofmisedvalues=[1,2,3,"apple","banana",3,4.5,5.6,6.7,True]

#print(listofitems[2])

#dictionaries are the collection of items which are unordered, changeable and indexed. They have keys and value pairsThey have keys and values.

myfirst_dict = {
    "name": "sruthi",
    "age" : 43,
    "Location"  : "Edison"
}
print("Sruthi  lives in", myfirst_dict["Location"])

if myfirst_dict["age"] >40 :
    print("Sruthi is above 40 years old")
else :
    print("Sruthi is below 40 years old")


