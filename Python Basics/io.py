#NOTE THE FOLLOWING DOESN'T WORK BECAUSE THIS IS AN ONLINE COMPILER, NOT IN THE COMPUTER.

#testing = open("testing.py","xt") - opens a file. the 1st parameter = the file location : it could be relative(meaning it is in the same directory as this class, so you just specify the name) or you could name the whole hierarchy. 2nd parameter = mode(1st letter is what you want to do with the file, second letter is 't'-text or 'b'-binary, for images)

#the letter 'x' stands for creating a new file. THERE NEEDS TO BE NOTHING IN IT FROM BEFORE.
#'w' stands for write, so you can have stuff in the file from before, but what you write with the write method overrides it.
#'a' stands for append, so you can write things, saving the stuff already there before, but use the same write() method.
#'r' stands for read, so you read the text by printing it in this program:
#print(testing.read()) - parameter (optional) - # of characters you want to read(the first how many chars?)
#print(testing.readline()) - reads the first line - if you call it again, it reads the next line.
#testing.write("print(\"I hate eating fish!\")") - writes something in that file

#to delete file, use OS remove() method - FROM OS, you need to import: 
""" 
import os  
if os.path.exists("testing.py"):  - if the testing.py file exists, since if it doesn't exist, error occurs.
    os.remove("testing.py") - again you can use relative of write out the whole directory.

os.rmdir("DIRECTORY TO REMOVE") - use to delete directory, you can use the os.path.exists() again for this, too

"""
#like try-catch-finally in java:
try:#what it tries to do from the beginning
    testing = open("testing.py","xt")
    testing.write("print(\"I hate fish!\")")
except NameError:#if a NameError type error occurs, this is what you do, without throwing a tantrum/error:
    print("Name Error occurred")
except FileExistsError:#multiple excepts can happen, this one for FileExistsError
    print("This file already exists")
except:#if the type of error doesn't fit the above ones, execute this code.
    print("Error")
finally:#no matter what happens, at the end, do this:
    testing.close()#closes the object
    print("end of try")