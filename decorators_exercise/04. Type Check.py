def type_check(type):
    def decorator(fn):
        def wrapper(argument):
            if not isinstance(argument, type):
                return "Bad Type"
            return fn(argument)
        return wrapper
    return decorator


@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
