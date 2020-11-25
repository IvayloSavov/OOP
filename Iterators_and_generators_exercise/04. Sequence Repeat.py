class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.current_char_index = -1
        self.count = number

    def __iter__(self):
        self.count = self.number
        self.current_char_index = -1
        return self

    def __next__(self):
        if self.count > 0:
            self.count -= 1
            self.current_char_index += 1
            self.current_char_index %= len(self.sequence)
            return self.sequence[self.current_char_index]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
