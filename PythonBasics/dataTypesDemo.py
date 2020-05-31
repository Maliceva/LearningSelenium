 # List data type

# Declares a list type variable called "values" that contains multiple data types within it
values = [1, 2, "cat", 4, 5.5]

# Returns everything in the list
print(values)

# Returns first item in the list
print(values[0])

# Returns last item in the list
print(values[-1])

# Returns multiple values in the list in order (starting at the second list item and ending at the third)
print(values[1:3])

# Add data to the list starting at position 3
values.insert(3,"dog")
print(values)

# Add data to the end of the list
values.append("End")
print(values)

# Update existing list data at a specific spot
values[2] = "CAT"
print(values[2])

# Delete value from list data at a specific spot
del values[0]
print(values)







# Tuple data type (like list, but write protected - can't be modified)

# Declare a tuple variable
val = (1, 2, "cat", 4.5)

# Attempt to a single value from a tuple - will throw an error at runtime
#val[2] = "CAT"







# Dictionary data type - hashmap in Java, like list but with key values

# Declares a dictionary
# Key values can be string or integer, only syntax that matters is {} around the list and : after the key value
dic = {"a":2, 4:"bcd", "c":"Hello"}

# Returns a dictionary value by key
print(dic[4])
print(dic["c"])

# Creates an empty dictionary
dict = {}

# Pass values to the dictionary at runtime
dict["firstname"] = "Cassandra"
dict["lastname"] = "Reitz"

print(dict)
print(dict["lastname"])