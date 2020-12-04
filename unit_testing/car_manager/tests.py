from .car import Car
import unittest


class CarTests(unittest.TestCase):

    def setUp(self) -> None:
        self.car = Car('a', 'b', 1, 4)

    def test_init(self):
        self.assertEqual(self.car.make, "a")
        self.assertEqual(self.car.model, "b")
        self.assertEqual(self.car.fuel_consumption, 1)
        self.assertEqual(self.car.fuel_capacity, 4)
        # self.assertEqual(self.car.fuel_amount, 0)

    def test_make_empty_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.make = ""
        # self.assertEqual(str(exc.exception), "Make cannot be null or empty!")
        # self.assertRaises(Exception, self.car.model, "")

    def test_model_empty_raises_exception(self):
        with self.assertRaises(Exception) as exc:
            self.car.model = ""
        # self.assertEqual(str(exc.exception), "Model cannot be null or empty!")

    def test_fuel_consumption_negative_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_consumption = -1

    def test_fuel_capacity_negative_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.fuel_capacity = -1

    def test_refuel_negative_raises_exception(self):
        with self.assertRaises(Exception):
            self.car.refuel(-1)

    def test_refuel_more_than_capacity(self):
        self.car.refuel(42)
        self.assertEqual(self.car.fuel_amount, self.car.fuel_capacity)

    def test_drive_more_than_fuel(self):
        with self.assertRaises(Exception) as exc:
            self.car.drive(1000)
        self.assertEqual(str(exc.exception), "You don't have enough fuel to drive!")

    def test_fuel_amount_after_drive(self):
        self.car.refuel(4)
        self.car.drive(400)
        self.assertEqual(self.car.fuel_amount, 0)


if __name__ == "__main__":
    unittest.main()