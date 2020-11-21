from itertools import permutations


def possible_permutations(l: list):
    for perm in permutations(l):
        yield list(perm)


[print(n) for n in possible_permutations([1, 2, 3])]