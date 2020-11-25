class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = dictionary
        self.__work_dictionary = self.dictionary.copy()
        self.__iterator = iter(self.dictionary.items())
    #
    # def __iter__(self):
    #     return self

    def __iter__(self):
        self.__iterator = iter(self.dictionary.items())
        # return iter([(k, v) for k, v in self.dictionary.items()]) # Така няма нужда от next но в judge гълрми
        return self.__iterator

    # def __next__(self):
    #     for k, v in self.__work_dictionary.items():
    #         res = (k, v)
    #         self.__work_dictionary.pop(k)
    #         return res
    #     raise StopIteration

    def __next__(self):
        val = next(self.__iterator)
        return val


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
