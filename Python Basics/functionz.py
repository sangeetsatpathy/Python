x=17
def functionExample(x="zero"):#defining a function (def keyword important) - in the parentheses, the arguments go in. If you set an equals sign and assign the parameter to a value, that is the default value if nobody puts in the parameter when calling the function
    print("this is function example number "+x)
functionExample("one")#calling a function, you have to pass in a parameter. To define data type, you simply enter the right one.
functionExample() #uses default value of 'zero'

def average(a,b):
    if a==0 and b==0:
        return "Go away."#if these 2 conditions are met, and we print 'Go away,' then we are breaking the definition - the return acts like a break because there can be only one return, the return value is the end of a def.
    avg = (a+b)/2
    return avg#returns a value to us

print(average(input("First number to average: "), input("Second number to average: ")))#prints the average value that was returned
def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)#recursion - when you call a method inside its own method definition. Basically, it keeps calling the method inside those parentheses, until it returns one to the innermost factorial method, solving the outermost one.
#for example, factorial(4)
#f(4)=4*f(3) - after computing f(3), compute f(4), and then return it
#f(3)=3*f(2) - after computing f(2), computes f(3)
#f(2) = 2*f(1)  - later, after figuring out f(1), computes f(2)
#f(1) = 1, as defined earlier in the expression
#this all keeps simplifying and computing because when the computer wants to return the answer, they can't return 4*f(3) - they have to find out f(3), so they keep going.

b = lambda a: a+10#a lambda is a short, anonymous function
#the variable(s) before the colon are the variables that are in the function - after the colon, it is the function to be used.
c=b(3)#calls the b function (which is now a function because it was assigned a lambda value), giving a the value of 3.

#the power of lambda
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)#passing in 2 as the value of n
#mydoubler becomes a lambda function, so when you call it ot pass in parameters, it passes in the value for the lambda
print(mydoubler())#passing in 11 as the value of a
