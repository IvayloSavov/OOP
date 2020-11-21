def squares(n):
    for n in range(1, n + 1):
        yield n ** 2


print(list(squares(5)))

squares = lambda n: (i ** 2 for i in range(1, n + 1))
