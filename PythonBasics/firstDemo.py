print("howdy")

# single line comment syntax

# declaring a variable doesn't require you to specify a type (data type is determined at runtime)
a = 3
print(a)

Str = "Hello world"
print(Str)

# defining multiple variables in a single line
b, c, d = 5, 6.4, "cat"
print(b)
print(c)
print(d)

# semicolons are not required but indentation is noticed by pycharm (has intellisense built in)

# You can't concatenate strings and integers like in other languages. This will not work:
# print("Value is " + b)
# Correct syntax: number of {} for each value, specify what values in parentheses
print("{} {}".format("Value is ", b))

# How to find out what data types are being set to variables:
print(type(b))
print(type(c))
print(type(d))
# More about Python data types: https://www.journaldev.com/14036/python-data-types





