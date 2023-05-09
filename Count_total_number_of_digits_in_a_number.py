# Write a program to count the total number of digits in a number using a while loop.
counter = 0
num = int(input("Enter a Number : "))

while num !=0 :
    # floor division
    # to reduce the last digit from number
    num = num // 10

    # increment counter by 1
    counter += 1

print("Total digits are : ", counter) 
