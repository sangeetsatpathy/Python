
#String concatenation works in python like java.
string = "helooloh"
print(len(string))#length of string
print(type(string))#type() method returns the data type
print(string[1:5])#indeces start at 0, strings are charArays like in java (except no char data type in python)
print(string[4]*50)
string2="     sup my dudes i am THE KING    "
print(string2.strip())#.strip() takes out spaces in front and after string that aren't needed. if you specify the chars in the brackets, it takes out those chars.
string3 = "shut up"
print(string3.capitalize())#str.capitalize() method capitalizes first char
print(string3.upper())#capitalizes it all
print((string2.strip()).lower())#lowercases it all, after taking out front and back spaces.
print(string3.replace(string3[3:5],"hi"))#replaces old indeces (you could just specify all the letters) with "hi".
print(string.split('l'))#splits the str every time an 'l' occurs into an array of a number of strings, split (and exclusive of) the 'l'
name = input("What is ur name?")#takes in input by typing in terminal and stores in 'name' var (input is always a string w/ this method) parameter = prompt.
print("Hello "+name)
print(10//4)# should be 2.5, but double division(//), called FLOOR DIVISION, gets rid of everything behind the decimal point.
print(10**2)#10^2 (**=exponent)
greaterOne = input("a number greater than one: ")


if 1<int(greaterOne):#casting - surround the component to change w/ parentheses and name the data type to change it to outside (works from string to number as long as it is possible).
    print("I KNOW ALGEBRA!!!")
elif 1==int(greaterOne):#else if
    print("I am so bad at being a kinder...")
else:
    print("WHAT WILL I DO?")

print("This is a {} statement".format('test'))#every time there is a curly brace, it is a placeholder. The .format() method takes in parameters - the values of each of the placeholders.
