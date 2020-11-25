from typing import Callable


def even_parameters(fn: Callable) -> Callable:
    def wrapper(*args):
        for n in args:
            if not isinstance(n, int) or n % 2 != 0:
                return "Please use only even numbers!"
        return fn(*args)
    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result


print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))


@even_parameters
def add(a, b):
    return a + b


print(add(2, 4))
print(add("Peter", 1))

