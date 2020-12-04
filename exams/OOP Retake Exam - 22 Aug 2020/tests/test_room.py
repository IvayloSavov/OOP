import unittest

from project.rooms.room import Room


class RoomTest(unittest.TestCase):
    def setUp(self) -> None:
        self.room = Room("Double", 100, 2)

    def test_can_be_create_an_instance(self):
        Room("Double", 100, 2)

    def test_attributes(self):
        self.assertEqual(self.room.family_name, "Double")
        self.assertEqual(self.room.budget, 100)
        self.assertEqual(self.room.members_count, 2)
        self.assertEqual(len(self.room.children), 0)

    def test_expenses_value_error(self):
        with self.assertRaises(ValueError) as exc:
            self.room.expenses = -10
        self.assertEqual(str(exc.exception), "Expenses cannot be negative")

    def test_expenses_correct_set(self):
        res = self.room.expenses = 10
        self.assertEqual(res, 10)

    def test_property_expenses(self):
        self.assertEqual(self.room.expenses, 0)

    def test_custom_calculate_expenses(self):
        self.children = [10, 10]
        self.assertEqual(self.room.calculate_expenses(self.room.children, self.room.appliances), 0)
        self.assertEqual(self.room._expenses, 0)

    def test_custom_str_enough_budget(self):
        res = repr(self.room)
        self.assertEqual(f"{self.room.family_name} paid {self.room.expenses + self.room.room_cost:.2f}$ and have {self.room.budget:.2f}$ left.\n", res)

    def test_custom_str_not_enough_budget(self):
        self.room.budget = -1
        self.assertEqual(repr(self.room), f"{self.room.family_name} does not have enough budget and must leave the hotel.\n")
















