# Check if a number is prime:

inputNum = int(input("Number: "))

isPrime = True

if inputNum <= 1:
    print("Number should be greater then 1")
    
else:
    for i in range(2, inputNum):
        if (inputNum % i) == 0:
            isPrime = False
            break
    print(inputNum, "is prime:", isPrime)

print("python")