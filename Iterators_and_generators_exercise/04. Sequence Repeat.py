class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.current_char_index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.number > 0:
            self.number -= 1
            self.current_char_index += 1
            self.current_char_index %= len(self.sequence)
            return self.sequence[self.current_char_index]
        raise StopIteration


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')
