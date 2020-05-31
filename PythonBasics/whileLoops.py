it = 10

# While loops are used to check a condition. If it's true, it will continue executing.
# The loop will only stop when the condition becomes false.
# You can use if statements inside of a loop
# break ends the loop
# continue means to skip all the rest of the steps in the current iteration and move on to the next one
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 3:
        break # break ends the loop
    print(it)

    it = it - 1

print("While loop execution ended.")

