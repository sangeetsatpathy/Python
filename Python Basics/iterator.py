myList= [1,2,3,4,5]
myIter=iter(myList)#creates an iterator over the list
#iter(the iterable item) creates an iterator
print(next(myIter))#the next method returns the next item from the iterator - 1st arg = the iterator, 2nd arg (optional) gives a default so if the iterator is exhausted, it won't raise error but will give default.
print(next(myIter))
print(next(myIter))
print(next(myIter))
print(next(myIter))#5 times to go through all of the myList
#not so useful, can use it in a loop

class mySeq:
    def __iter__(self):#modifies iter so that a mySeq object can be passed in
        self.current=0
        return self#returns the new, modified object instance, including current var.
    def __next__(self):
        if self.current<=20:
            self.current+=5#modifies the next method to increment by 5
            return self.current
        else:
            raise StopIteration#if exceeds 20, raises StopIteration error/exception

s=mySeq()
myIter2 = iter(s)#stores the modified mySeq object(w/current var=0) in the myIter2 variable, so myIter2 is an object
print(next(myIter2))#returns 5 because next increments to 5
print(next(myIter2))#returns 10
print(next(myIter2))#returns 15
print(next(myIter2))#returns 20 - no limit as long as you keep calling it(except for the fact that i defined it so that it will return 20 at most or it will give error), since mySeq object has no ending, unlike list
for x in myIter2:
    print(x)#prints each number until the limit-automatically, so no error(in this case, 20)