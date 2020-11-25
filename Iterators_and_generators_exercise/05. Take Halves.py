def solution():
    def integers():
        n = 1
        while True:
            yield n
            n += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        res = [s for _, s in zip(range(n), seq)]
        # for integer in seq:
        #     res.append(integer)
        #     n -= 1
        #     if n == 0:
        #         break
        return res

        # for _ in range(n):
        #     yield next(seq)

        # for _ in zip(range(n), seq):
        #     yield next(seq)

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
