# This class is a child of Calculator from oopDemo.py
# Child classes inherit the methods and variables from their parent class
# Test cases will always be children of a parent class
# The parent filename has to be imported in order to create a parent/child class relationship
from oopDemo import Calculator

class ChildImpl(Calculator): # parent class name should be passed here
    num2 = 200

    # must call parent constructor inside the child constructor to get the parent's constructor
    def __init__(self):
        Calculator.__init__(self, 2, 10)

    def getCompleteData(self):
        return self.num2 + self.num + self.Summation()


obj = ChildImpl()
print(obj.getCompleteData())
