# Example:
# Read the file and store all the lines in a list
# Reverse the list
# Write the reversed list back to the file

# r = read mode
# w = write mode

# Create a reader object and open the file in read mode
with open('test.txt', 'r') as reader: # Optimized way of opening and closing a file
    content = reader.readlines() #[abc, asdfasd, cat, dog, 123]
    reversed(content) # [123, dog, cat, asdfasd, abc]

    # Create a writer object and update the file with the reversed content
    with open('test.txt', 'w') as writer:
        for line in reversed(content):
            writer.write(line)