#Dunder methods don't need to be called with their underscores: __add__ is just a + sign(like most arithmetic dunders), __repr__ is called repr(), __str__ is str(), __len__ is len(), and __init__ is in the object instantiation brackets. Every built in action comes from dunder methods.
#__name__ is a method returning the file name
class Employee:
#dunder methods serve a similar purpose to operator overloading in other languages - which means that you tell the computer HOW to do the arithmetic operation with objects - otherwise an error will appear
#Dunder methods allow us to define our class's behavior - bending the rules python set on us.
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)
    
    def __repr__(self):#repr is meant to be used by a developer - be unambiguous
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):#str is meant to be readable - put repr first, then str, so repr can be the fallback for str, should it fail.
        return '{} - {}'.format(self.fullname(), self.email)
    #each object data type has their own dunder add method.
    def __add__(self, other):#when you do an arithmetic add, they refer to this special method - if you don't override it, there will be a TypeError - you can't add to objects unless you specify how.
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())#you can use the function inside itself, except it returns a modified version

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print(emp_1 + emp_2)#now you can add these normally, since you defined __add__

print(len(emp_1))
