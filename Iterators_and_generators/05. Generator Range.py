def genrange(param, param1):
    for n in range(param, param1 + 1):
        yield n


def genrange(start, end):
    while start <= end:
        yield start
        start += 1


genrange = lambda start, end: (n for n in range(start, end + 1))


genrange = lambda start, end: range(start, end + 1)
