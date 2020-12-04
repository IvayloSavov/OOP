import unittest
from solution import Person



class PersonTest(unittest.TestCase):
    def test_person_is_properly_initiated(self):
        person = Person("Ivo")
        self.assertEqual(person.name, "Ivo")


if __name__ == "__main__":
    unittest.main()