# Create a recursive function to calculate the factorial of a number: {Polymorphism}

def factorial(num):
    if num <= 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))