def fibonacci():
    n_1, n_2 = 0, 1
    while True:
        yield n_1
        next_n = n_1 + n_2
        n_1 = n_2
        n_2 = next_n


generator = fibonacci()
for i in range(5):
    print(next(generator))
