# Write a generator function that yields even numbers up to a specified limit:


# correct way
def evenGenerator(limit):
    for i in range(2, limit + 1, 2):
        yield i

for num in evenGenerator(10):
    print(num)

print("1st Executed")

# not good 
def evenGenerator1(limit):
    for i in range(2, limit + 1, 2):
        return i

print(evenGenerator1(10))

print("2nd Executed")


def evenGenerator2(limit):
    list = []
    for i in range(2, limit + 1, 2):
        list.append(i)
    return list

print(evenGenerator2(10))