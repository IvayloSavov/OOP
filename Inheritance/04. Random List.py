import random


class RandomList(list):
    def get_random_element(self):
        element = random.choice(self)
        self.pop(self.index(element))
        return element


rl = RandomList([1, 2, 3, 4, 5])
el = rl.get_random_element()
print(el)