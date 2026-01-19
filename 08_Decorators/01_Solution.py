# Problem 1: Timing Function Execution
# Write a decorator that measures the time a function takes to execute:

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        func_runtime = (end_time - start_time).__round__(4)
        print(f"{func.__name__} ran in {func_runtime} time")
        return result
    return wrapper

@timer
def example_func(n):
    time.sleep(n)

example_func(3)
example_func(2)