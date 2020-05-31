# Strings can be split, concatenated, stripped, and validated

str = "CassandraReitzQA.com"
str1 = "QA Engineer"
str2 = "CassandraReitz"
str3 = "   great  "

print(str[1]) # outputs the second letter in the string (a)

print(str[0:4]) # outputs first 4 letters in the string (Cass)

print(str + " " + str1) # concatenates two strings and outputs both

# extract text from string and check to see if the extracted text is present
# prints true if text matches, false if not
print(str2 in str)

# splits up a string on a specified character and outputs both separately
var = str.split(".")
print(var)
print(var[0])

# removes whitespaces from beginning and end of a string
print(str3.strip())

# remove only beginning whitespace
print(str3.lstrip())

# remove only ending whitespace
print(str3.rstrip())

