class Point:
    def __init__(self,a,b):#the __init__ indicates it is a constructor, and it takes in the self parameter. It is also a function, so you need to say def. Again, you can set defaults so we don't need to input any parameters.
        self.x = 0#usually create all the state attributes in contructor
        self.y = 0
        print(a,b)
        self.__name = "Sangeet"#double underscore means it is a private variable, so it will give an error if you access in another class. There is a trick to access the private variables, but there is a trust b/ween programmers that they won't use it.
        self._color="Red"#the one underscore at the beginning indicates that this variable is protected, meaning it shouldn't be changed in another class except with the getter and setter method that the developer usually sets to get the variable, and the setter sets the protected variable to a new variable. However, you can still access it without the getter/setter method, but there is a trust between the programmers that they won't.
    def MovePoint (self, newX, newY):
        self.x=newX #the self keyword refers to the object instance of the class in which the method is callled on. Self is just convention - but it is always the first parameter of any funtion
        self.y=newY#the object's y=newY.
        return newX,newY
    def getColor(self):#getter, returns the protected var
        return self._color
    def setColor(self, newColor):#setter, sets the variable to newColor.
        self.color = newColor
    
class TripleDimension(Point):#to make a child class, write parentheses after the class name, then put in the name of the parent class. When inheriting, with an object of the child class, you can call the parent class's methods and variables.
#If a method is in both the parent AND child class, that means the child class is overriding it, making a new copy of the method, so when called, it will go to that.
    def __init__(self):
        self.x=super.x#refer to the parent class using 'super' keyword
        self.y = super.y
        self.z = int(input("What is your z value: "))
    
myPoint = Point(21,321)#how to create an object instance in python. You must input 2 parameters (not self) because of constructor.
"""You can also just call the constructor method of the class instead of storing in a variable. For example, in a child class:
super().__init__()
"""

myPoint.MovePoint(21,13) #we don't have to define the self because when we call the method from the object instance, it is already satisfying the parameter.

anotherPoint = Point(10,10)
