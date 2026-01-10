# Countingof Positive numbers:

numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positiveNumCount = 0
negativeNumCount = 0

for num in numbers:
    if num > 0:
        positiveNumCount += 1
    elif num < 0:
        negativeNumCount += 1
print("Final count of all positive numbers:", positiveNumCount)
print("Final count of all negative numbers:", negativeNumCount)