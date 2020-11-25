def upper_case(say_hi_fn):
    def wrapper(*args):
        res = say_hi_fn(*args)
        return res.upper()
    return wrapper


@upper_case
def say_hi(name):
    return f"Hi {name}!"


print(say_hi("Ivaylo"))