from project.food.dessert import Dessert


class Cake(Dessert):
    CAKE_GRAMS = 250
    CAKE_CALORIES = 1000
    CAKE_PRICE = 5

    def __init__(self, name, price=CAKE_PRICE, grams=CAKE_GRAMS, calories=CAKE_CALORIES):
        super().__init__(name, price, grams, calories)
