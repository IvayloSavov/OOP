def read_next(*args):
    # for itr in args:
    #    for ch in itr:
    #         yield ch

    return (str(ch) for itr in args for ch in itr)


# read_next = lambda *args: (str(ch) for itr in args for ch in itr)

for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
