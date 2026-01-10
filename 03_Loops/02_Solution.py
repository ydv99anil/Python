# Sum of even numbers upto n:

num = int(input("Numbers:"))
numSum = 0

for i in range(1, num+1):
    if i % 2 == 0:
        numSum += i
print("Sum of all even numbers upto {} is: {}".format(num, numSum))