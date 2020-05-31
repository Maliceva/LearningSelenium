# To read or write to a file in python, it must be opened inside the .py file
# If it's in the same directory, use the filename. If not, use the full path
#file = open('test.txt')

# read all the contents of the file and output it to console
#print(file.read())

# read first 2 characters of the file (ab)
#print(file.read(2))

# read file line by line (one readline per line)
# don't use file.read and file.readline together - pick one or the other
#print(file.readline())
#print(file.readline())

#file.close()

# Loop through a file and print line by line using readLine method
#file = open('test.txt')
#line = file.readline()

#while line!="":
#    print(line)
#    line = file.readline()

#file.close()  # files must always be closed


# Read a file and store each line as an index
# ['abc\n', 'asdfasd\n', 'cat\n', 'dog\n', '123']
file = open('test.txt')

for line in file.readlines():
    print(line)

file.close()