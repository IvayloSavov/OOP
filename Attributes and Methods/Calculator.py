from functools import reduce
import operator


class Calculator:

    @staticmethod
    def add(*args):
        return reduce(operator.add, args)

    @staticmethod
    def divide(*args):
        return reduce(operator.truediv, args)

    @staticmethod
    def multiply(*args):
        return reduce(operator.mul, args)

    @staticmethod
    def subtract(*args):
        return reduce(operator.sub, args)
