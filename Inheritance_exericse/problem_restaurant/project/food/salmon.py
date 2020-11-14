from project.food.main_dish import MainDish


class Salmon(MainDish):
    SALMON_GRAMS = 22

    def __init__(self, name, price, grams=SALMON_GRAMS):
        super().__init__(name, price, grams)
