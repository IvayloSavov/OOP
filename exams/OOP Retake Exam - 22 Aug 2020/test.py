def test(cost, *args):
    print(args)
    print(sum([cost, *args]))


test(7, 1, 2, 3)