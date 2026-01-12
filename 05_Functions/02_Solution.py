# Create a function that takes two numbers as parameters and returns their sum:

num1 = float(input("Give number 1: "))
num2 = float(input("Give number 2: "))

def sumFunc(num1, num2):
    return num1 + num2

result = sumFunc(num1, num2)
print(num1, "+", num2, "=", result)