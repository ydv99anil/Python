# Create a lambda function to compute the cube of a number:

input = int(input("number: "))

cube = lambda x: x ** 3

# cube2 = cube()
# print(cube2(4))    # Ase hold nhii krr skte esko

result = cube(input)
print(result)