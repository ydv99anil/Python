# Problem 3: Cache Return Values
# Implement a decorator that caches the return values of a function, so that when it's called with the same arguments, the cached value is returned instead of re-executing the function:

import time


def cache_func(any_func):
    cache_value = {}
    def wrapper(*args):
        if args in cache_value:
            return cache_value[args]
        result = any_func(*args)
        cache_value[args] = result
        return result
    return wrapper

@cache_func
def any_func(a, b):
    time.sleep(4)
    return a + b

print(any_func(2,3))
print(any_func(2,3))
print(any_func(5,3))
print(any_func(5,3))