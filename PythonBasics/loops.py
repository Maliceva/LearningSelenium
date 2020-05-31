# If/Else loop
greeting = "Good morning!"

# Loop executing on a false condition
# Colon indicates the end of the condition (think opening braces)
# Indentation indicates where loop starts and ends
if greeting == "Good morning!":
    print("Condition matches.")
else:
    print("Condition does not match.")

print("If/else ended")
print("*********************************************")



# For loop
# Print each item in the list, then end the loop
obj = [2, 3, 5, 7, 9]
# i is the variable that will temporarily hold what we're iterating from obj
for i in obj:
    print(i)
print("*********************************************")

# Print each item in the list multiplied by 2
for h in obj:
    print(h*2)
print("*********************************************")

# Print the sum of the first natural numbers 1+2+3+4+5 = 15
summation = 0
for j in range(1, 6): # iterate 1 to 6-1
    summation = summation + j
print(summation)
print("*********************************************")

# For every loop, jump two indexes (print only odd numbers)
for k in range(1, 10, 5):
    print(k)
    print("SKIPPING FIRST INDEX")
for m in range(10):
    print(m)
print("*********************************************")
