# Write a program to use the loop to find the factorial of a given number.

# The factorial (symbol: !) means to multiply all whole numbers from the chosen number down to 1.

num = 5
factorial = 1
if num < 0:
    print("Factorial does not exist for negative numbers")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    # run loop 5 times
    for i in range(1, num + 1):
        # multiply factorial by current number
        factorial = factorial * i
    print("The factorial of", num, "is", factorial)