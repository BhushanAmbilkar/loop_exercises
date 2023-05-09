# Write a program to accept a number from a user and calculate the sum of all numbers from 1 to a given number

# For example, if the user entered 10 the output should be 55 (1+2+3+4+5+6+7+8+9+10)

# METHOD -- 01 

s = 0
num = int(input("Enter a Numer : "))

for i in range (1, num+1, 1):
    s += i 
print("\n")
print("Sum is : ", s)    


# METHOD -- 02      Using the built-in function sum()

n = int(input("Enter a Number : "))
# pass a range of numbers to sum() function
x = sum(range(1, n+1, 1))
print("Sum is : ", x)

