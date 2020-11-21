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
        res = []
        for integer in seq:
            res.append(integer)
            n -= 1
            if n == 0:
                break
        return res

    return take, halves, integers


take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
