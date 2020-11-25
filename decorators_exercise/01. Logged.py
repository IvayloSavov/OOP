def logged(fn):
    def wrapper(*args, **kwargs):
        res_of_fn = fn(*args, **kwargs)
        res_to_return = f"you called {fn.__name__}{args}\n"
        res_to_return += f"it returned {res_of_fn}"
        return res_to_return
    return wrapper


@logged
def sum_func(a, b):
    return a + b


print(sum_func(1, 4))
