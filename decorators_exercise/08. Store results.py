from functools import total_ordering

class store_results:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        with open("results.txt", "a") as f:
            res = self.func(*args, **kwargs)
            f.write(str(f"Function '{self.func.__name__}' was called. Result: {res}\n"))


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b


with open("results.txt", "w") as f: # cleaning the file before execution the program
    pass

add(2, 2)
mult(6, 4)

