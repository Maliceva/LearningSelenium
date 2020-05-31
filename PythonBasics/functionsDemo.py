# A function is a group of related statements that perform a specific task.

# def creates a function
# indentation specifies beginning and end of the function
# pyCharm recommends having two lines between functions
# return lets you save the value inside a function


def GreetMe(name):
    print("Good morning, "+name)


# Calls the GreetMe function
GreetMe("Cassandra")


def AddIntegers(a, b):
    return a+b


print(AddIntegers(2, 3))