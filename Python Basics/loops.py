#Loops

#For loops - in python, used to loop with every element of a list, tuple, dictionary, or String.
listVar2 = ["Netflix", "Amazon", "Youtube", "Hulu"]
for c in listVar2: #c is iterator and is declared to be in listVar. NOTE: c is global variable, when called after, it will return the last iteration, for this example it is "Hulu"
    print(c)#prints each element, then loops again till every element is printed - you can do the same for a string

for i in range(1,4,1):#range() method is the range; in example, it will print every element in listVar2 from index one to index 3. 1st parameter = start (optional), second parameter = end(exclusive). Without start, it will start from 0. 3 parameter (optional) is the increment. The start and end numbers and inbetween entail all the VALUES OF I.
    if listVar2[i]=="Hulu":
        break #break statement exits the loop, used with an if statement.
    print(listVar2[i])

#for a for loop with a dictionary, the iterator is the KEY.

k=0#while loops are more for conditions, instead of iterating through data sets.
while k<10:#while this statement is true, the code will keep repeating
    if k==4 or k==8:
        continue #continue keyword SKIPS the current ITERATION, so in this case, you don't see 4 or 8, but you see 0, 2, and 6.
    print(k)
    i+=2#increment