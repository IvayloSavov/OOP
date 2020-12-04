from test_cat.solution import Cat
import unittest


class CatTests(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Joe")

    def test_init(self):
        self.assertEqual(self.cat.name, "Joe")

    def test_increase_size_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.size, 1)

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)

    def test_cannot_eat_if_fed(self):
        self.cat.eat()
        with self.assertRaises(Exception) as exc: # the ContextManager catches the exception and doesn't raise it
            self.cat.eat()
        self.assertEqual(exc.exception.args[0], "Already fed.")

    def test_cannot_sleep_if_not_fed(self):
        with self.assertRaises(Exception) as exc:
            self.cat.sleep()
        self.assertEqual(exc.exception.args[0], "Cannot sleep while hungry")

    def test_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertFalse(self.cat.sleepy, False)


if __name__ == "__main__":
    unittest.main()
