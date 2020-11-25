from pprint import pprint


def cache(fn):
    log = {}

    def wrapper(args, **kwargs):
        if args not in log:
            res = fn(args, **kwargs)
            log[args] = res
            return res
        return log[args]
    wrapper.log = log
    # wrapper.name = "Fibonacci"
    return wrapper


@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


# fibonacci.name = "Pesho"
fibonacci(100)
pprint(fibonacci.log)
# print(fibonacci.name)
