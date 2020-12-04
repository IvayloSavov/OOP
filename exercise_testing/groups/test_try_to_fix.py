import unittest


class PersonTest(unittest.TestCase):
    def setUp(self) -> None:
        self.person = Person("Ivaylo", "Savov")

    # def test_init(self):
    #     self.assertEqual(self.person.name, "Ivaylo")
    #     self.assertEqual(self.person.surname, "Savov")

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
        person_1 = Person("Ivaylo", "Savov")
        person_2 = Person("Bogomila", "Vateva")
        people = [person_1, person_2]
        self.group = Group("SoftUni", people)

    # def test_init(self):
    #     self.assertEqual(self.group.name, "SoftUni") # TODO: Maybe they don't want the initialization
    #     self.assertEqual(len(self.group), 2)
    #     self.assertIn(self.person_1, self.group.people)
    #     self.assertIn(self.person_2, self.group.people)

    def test_add(self):
        person_3 = Person("Snezhanka", "Mitova")
        person_4 = Person("Kiril", "Mitov")
        group_2 = Group("Family", [person_3, person_4])
        new_group = self.group + group_2
        # self.assertEqual(new_group.name, "Family")
        self.assertEqual(len(new_group), 4)

    def test_len(self):
        self.assertEqual(len(self.group), 2)

    def test_getitem(self):
        result = self.group[0]
        self.assertEqual(self.group[0], 'Person 0: Ivaylo Savov')

    def test_repr(self):
        res = str(self.group)
        self.assertEqual(res, f'Group SoftUni with members Ivaylo Savov, Bogomila Vateva')


if __name__ == "__main__":
    unittest.main()