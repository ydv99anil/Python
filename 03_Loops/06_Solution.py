# Compute the factorial of a number using a while loop:

number = int(input("Number: "))
orginalNumber = number
factorial = 1

while number > 0:
    factorial = factorial * number
    number = number - 1
print("Factorial of {} is: {}".format(orginalNumber, factorial))