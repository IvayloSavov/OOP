def get_primes(l: list):
    for n in l:
        is_not_prime = False
        if n > 1:
            for div_n in range(2, n):
                if n % div_n == 0:
                    is_not_prime = True
                    break
            if not is_not_prime:
                yield n


print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))