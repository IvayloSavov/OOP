class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.__work_dictionary = self.dictionary.copy()

    def __iter__(self):
        return self

    def __next__(self):
        for k, v in self.__work_dictionary.items():
            res = (k, v)
            self.__work_dictionary.pop(k)
            return res
        raise StopIteration()


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
