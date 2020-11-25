VOWELS = {"A", "E", "I", "O", "U"}


def vowel_filter(fn):
    def wrapper(*args, **kwargs):
        res = fn(*args, **kwargs)
        return [c for c in res if c.upper() in VOWELS]
    return wrapper


def make_upper(fn):
    def wrapper(*args, **kwargs):
        result = fn(*args, **kwargs)
        return [c.upper() for c in result]

    return wrapper


@vowel_filter
@make_upper
def get_letters():
    return ["a", "b", "c", "d", "e"]

# get_letters = make_upper(get_letters)
# get_letters = vowel_filter(get_letters)

# get_letters = vowel_filter(make_upper(get_letters))

print(get_letters())
