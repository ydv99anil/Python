# Write a function that takes variable number of arguments and returns their sum:



def sumAll(*args):
    print(args)
    for i in args:
        print(i ** 2)
    return sum(args)

print(sumAll(1,2,3))
