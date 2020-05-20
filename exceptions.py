# Examples of exception handling: raise, pass, assert, try except, and finally

ItemsInCart = 0
# Add 2 items to cart via automation


# Check to see if the cart count is valid
#if ItemsInCart != 2:
    #raise Exception("Cart total is invalid. Expected 2.")
    #pass

# Expects a condition that will always be true
# if condition is false, an "AssertionError" will be thrown and the condition will be displayed
#assert(ItemsInCart == 2)

# Try to do something, if it fails, catch the error (except)
# Code in the Except block will not be executed if the code in the try block runs successfully
# Code in the finally block executes every time, regardless of whether the try and except blocks execute
try:
    with open('filelog.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e) # captures the actual error from Python
    print ("Reached this block because the code in the Try block failed.")

finally:
    print("Cleaning up resources") #put teardown methods here (example: clearing cookies)