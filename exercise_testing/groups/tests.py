from groups.solution import Person
from groups.solution import Group
import unittest


class PersonTest(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person("Ivaylo", "Savov")

    def test_init(self):
        self.assertEqual(self.person.name, "Ivaylo")
        self.assertEqual(self.person.surname, "Savov")

    def test_repr(self):
        self.assertEqual(str(self.person), "Ivaylo Savov")

    def test_add(self):
        person_2 = Person("Bogomila", "Vateva")
        new_person = self.person + person_2
        # self.assertEqual(type(new_person), Person)  # TODO: this may be is a problem, only test the names?
        self.assertEqual(new_person.name, "Ivaylo")
        self.assertEqual(new_person.surname, "Vateva")


class GroupTest(unittest.TestCase):
    def setUp(self) -> None:
        people = [Person("Ivaylo", "Savov"), Person("Bogomila", "Vateva")]
        self.group = Group("SoftUni", people)

    def test_init(self):
        self.assertEqual(self.group.name, "SoftUni") # TODO: Maybe they don't want the initialization
        self.assertEqual(len(self.group), 2)

    def test_add(self):
        group_2 = Group("Family", [Person("Snezhanka", "Mitova"), Person("Kiril", "Mitov")])
        new_group = self.group + group_2
        self.assertEqual(len(new_group), 4)

    def test_len(self):
        self.assertEqual(len(self.group), 2)

    def test_getitem(self):
        self.assertEqual(self.group[0], 'Person 0: Ivaylo Savov')

    def test_iteration_should_return_info_for_the_people(self):
        self.assertEqual(list(self.group), [
            "Person 0: Ivaylo Savov",
            "Person 1: Bogomila Vateva",

        ])

    def test_repr(self):
        res = str(self.group)
        self.assertEqual(res, f'Group SoftUni with members Ivaylo Savov, Bogomila Vateva')


if __name__ == "__main__":
    unittest.main()