# classes are a user defined blueprint or prototype
# A "calculator" class would have functions for sum, multiplication, addition, etc.
# Classes have methods, class variables, instance variables, constructors, etc.
# Constructors are methods that are automatically called in a class
# Class variables are declared at the class level
# Instance variable are declared inside the object and are sent to the class
# Self keyword is mandatory for calling variable names into method
# Instance and class variables have different purposes
# Constructor name should always be __init___
# New keyword is not required when creating objects

class Calculator:
     num = 100 #class variable

     def __init__(self,a,b): # default constructor (always __init__)
         self.firstNumber = a #instance variable
         self.secondNumber = b #instance variable
         print("I am called automatically when the class object is created.")

     def getData(self):
         print("I am now executing as a method in a class.")

     def Summation(self):
        return self.firstNumber + self.secondNumber + Calculator.num

# Declare the class as an object:
obj = Calculator(2, 3)

# Execute the method inside the class
obj.getData()
print(obj.Summation())

# Classes can be called multiple times by creating new objects:
obj2 = Calculator(4, 5)
obj2.getData()
print(obj2.Summation())