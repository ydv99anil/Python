# Problem 2: Debugging Function Calls
# Create a decorator to print the function name and the values of its arguments every time the function is called:

def print_function(func):
    def wrapper(*args, **kwargs):

        args_values = ", ".join(str(arg) for arg in args)
        # kwargs_values = ", ".join(str(key = value) for key, value in kwargs.items())  #** Lesss Effective **

        kwargs_values = ", ".join(f"{key}={value}" for key, value in kwargs.items())
        print(f"Calling {func.__name__} with args: {args_values} and kwargs: {kwargs_values}")
        return func(*args, **kwargs)
    return wrapper


@print_function
def greet(name, greeting = "Hello"):
    print(f"{greeting}, {name}")

greet("Anil", greeting = "Namaste!")


""" def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{k}={v}" for k, v in kwargs.
        items())
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs_value}")
        return func(*args, **kwargs)
    
    return wrapper

@debug
def hello():
    print("hello")

@debug
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}")

hello()
greet("chai", greeting="hanji ") """