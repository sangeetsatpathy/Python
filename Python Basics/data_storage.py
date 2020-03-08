#Data types
#Lists like arrays, but can hold more than one type of value at a time, can repeat. You can use the length (len(listVar)) for lists and tuples.
listVar = ["apple","google","stuff",21,"google"]
listVar[2] = "Microsoft"
if "google" in listVar:#in keyword checks if an element is in the list - can be use w/ any data structures(sets, tuples, dictionaries)
    print("Google is in listVar")
else:
    print("Google is not in listVar")
listVar.append("Amazon")#adds object
listVar.insert(2, "Dell")#adds, but at a specific index
listVar.remove(21)#remove - if 2 of the same value, deletes only the first one, if not there already, gives error.
del listVar[0]#del keyword is deletes, so it deletes listVar's 0 index.
listVar.clear()#deletes all the elements of listVar

#Tuple like lists, but you cannot change the value of any of the items, can repeat, more than one type of data type at a time.
tupleVar = ("apple","google","stuff",21,"google")
tupleVar.index("apple")#returns index of a value


"""Set doesn't support duplicates of values (can't repeat - no error, but there simply won't be a second item), and
you cannot call any specific index of it - you use the whole thing or nothing. Order doesn't matter. It's more like
sets in math."""
mySet = {"apple","google","stuff",21,"google"} # no error, but second google won't appear
myOtherSet = {"apple","other stuff","yahoo"}
mySet.add("Microsoft") #adds something
mySet.update(["orange","gksj"])#updates a set w/ union of itself and others MAKE SURE TO INCLUDE THE SQUARE BRACKETS, TOO.
print(mySet)
print(len(mySet))#length of mySet
mySet.remove("apple")#removes it from the set.
mySet.discard("akfje")#removes, but doesn't give error if that element isn't there.
print(mySet)
mySet.union(myOtherSet)#makes a union of elements(in math, when a double inequality of 'or' operator, solution called union.) If there is a duplicate, it says it only once in both the sets (it combones them - the sets are the solutions, mathematically speaking - one or the other).
mySet.intersection(myOtherSet)#makes an intersection of elements, in math called the AND operator. It gives the object that are in both sets only - since it is returning the AND values.
mySet.difference(myOtherSet)#ONLY objects in mySet that aren't in myOtherSet (like subtracting it.)

#Dictionaries are another data storage system, like list.
example_Dictionary = {
    "Brand":"Apple", # a dictionary has multiple data storage indeces, each separated by commas.
    "Machine":"iPhone", #each index is a pair : the key and the value of the key
    "Model" : "Xs",
    "Year" : 2018 #can be different types of data values at the same time
}
yesno = "X" in example_Dictionary.values() # is 'X' in values of example_Dictionary?
example_Dictionary["Price"] = 1005.99 #adds a price key, with its value
example_Dictionary["Year"] = 2019 #changes the year key to 2019.
brand = example_Dictionary["Brand"] #stores the value, 'Apple' in the brand variable - access value by calling the key of the key value inside square brackets, like in lists(does same thing if you say example_Dictionary.get(Brand))
#in a for loop with a dictionary, the iterator is the KEY(say it's x), so you can say print(example_Dictionary[x]), and it will print the values:
""" for x in example_Dictionary:
        print(example_Dictionary[x])
    or
    for x in example_Dictionary.values(): - the dicionary.values() method allows us to access the values
        print(x)  - x is the values"""
""" You can also print pair of the dictionary:
for x,y in example_Dictionary.items():
    print(x,y) - prints the pair"""