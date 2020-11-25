class countdown_iterator:
    def __init__(self, count):
        self.count = count
        self.__current = count

    def __iter__(self):
        self.__current = self.count
        return self

    def __next__(self):
        if self.__current >= 0:
            number = self.__current
            self.__current -= 1
            return number
        raise StopIteration

iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
