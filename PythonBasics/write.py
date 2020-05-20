# Read the file and store all the lines in the list
# Reverse the list
# Write the reversed list back to the file
with open('data.txt', 'r') as reader:
    content = reader.readlines() # [cat, dog, 1, 2, 3, 4, 5]
    reversed(content) # [4, 3, 2, 1, dog, cat]

    with open('data.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)
