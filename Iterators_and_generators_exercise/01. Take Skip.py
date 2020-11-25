class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.current_number = 0

    def __iter__(self):
        self.current_number = 0
        return self

    def __next__(self):
        # generated_so_far = val / self.step
        # if self.count == generated_so_far:
        #     raise StopIteration
        if self.count > 0:
            number = self.current_number
            self.current_number += self.step
            self.count -= 1
            return number

        raise StopIteration

numbers = take_skip(10, 5)
for number in numbers:
    print(number)

