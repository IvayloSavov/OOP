import unittest
from vehicle.solution import Car, Truck


class CarTest(unittest.TestCase):
    def setUp(self) -> None:
        self.car = Car(100, 1)

    def test_init(self):
        self.assertEqual(self.car.fuel_quantity, 100)
        self.assertEqual(self.car.fuel_consumption, 1)

    def test_refuel(self):
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_quantity, 110)

    # def test_increased_fuel(self):
    #     self.assertEqual(self.car._INCREASED_FUEL, 0.9)

    def test_drive_not_enough_fuel(self):
        self.car.drive(1000)
        self.assertEqual(self.car.fuel_quantity, 100)

    def test_drive_enough_fuel(self):
        self.car.drive(10)
        self.assertEqual(self.car.fuel_quantity, 81)


class TestTruck(unittest.TestCase):
    def setUp(self) -> None:
        self.truck = Truck(100, 1)

    def test_init(self):
        self.assertEqual(self.truck.fuel_quantity, 100)
        self.assertEqual(self.truck.fuel_consumption, 1)

    def test_refuel(self):
        self.truck.refuel(10)
        self.assertEqual(self.truck.fuel_quantity, 109.5)

    # def test_increased_fuel(self):
    #     self.assertEqual(self.truck._INCREASED_FUEL, 1.6)

    def test_drive_not_enough_fuel(self):
        self.truck.drive(1000)
        self.assertEqual(self.truck.fuel_quantity, 100)

    def test_drive_enough_fuel(self):
        self.truck.drive(10)
        self.assertEqual(self.truck.fuel_quantity, 74)


if __name__ == "__main__":
    unittest.main()