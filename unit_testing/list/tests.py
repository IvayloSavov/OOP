from .extendet_list import IntegerList
import unittest


class IntegerListTests(unittest.TestCase):
    def setUp(self):
        self.list = IntegerList([])

    def test_add(self):
        self.assertEqual(self.list.add(42), [42])

    def test_add_raises_value_error(self):
        self.assertRaises(ValueError, self.list.add, "baba")
        # with self.assertRaises(ValueError) as exc:
        #     self.list.add("str")
        # self.assertEqual(exc.exception.args[0], "Element is not Integer")

    def test_remove_by_index(self):
        self.list.add(42)
        eq = self.list.remove_index(0)
        self.assertEqual(eq, 42)

    def test_remove_by_index_raises_index_error(self):
        self.assertRaises(IndexError, self.list.remove_index, 10)

    def test_init_takes_only_ints(self):
        list = IntegerList("baba", 42, "dqdo")
        self.assertEqual(list.get_data(), [42])

    def test_get(self):
        self.list.add(42)
        self.assertEqual(self.list.get(0), 42)

    def test_add_non_int(self):
        self.assertRaises(ValueError, self.list.add, "43")

    def test_get_raises_index_error(self):
        self.assertRaises(IndexError, self.list.get, 5)

    def test_insert(self):
        self.assertRaises(IndexError, self.list.insert, 0, 42)
        self.list.add(1)
        self.assertRaises(ValueError, self.list.insert, 0, "dqdo")
        self.list.insert(0, 42)
        self.assertEqual(self.list.get_data(), [42, 1])

    def test_the_biggest(self):
        self.list.add(2)
        self.list.add(3)
        self.assertEqual(self.list.get_biggest(), 3)

    def test_get_index(self):
        self.list.add(42)
        self.assertEqual(self.list.get_index(42), 0)


if __name__ == "__main__":
    unittest.main()