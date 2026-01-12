# Write a function that greets a user. If no name is provided, it should greet with a default:

name = input("your name: ")

def greetFunc(name):
    if name:
        return "Hello, " + name + "!"
    else:
        return "Hello! how are you?"

print(greetFunc(name))

# Method 2nd:
name2 = input("Name:")
def greetFunc(name2 = "User"):
    return "Hello, " + name2 + "!"

print(greetFunc(name2))
print(greetFunc())