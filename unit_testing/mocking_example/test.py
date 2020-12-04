import unittest
from unittest import mock
from mocking_example import solution


class SolutionTests(unittest.TestCase):

    # def test_get_my_daily_tasks(self): # without mocking
    #     daily_task = solution.my_daily_todo()
    #     self.assertEqual(daily_task, [{"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False}])

    def test_get_my_daily_tasks(self):  # with mocking
        mock_value = {"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False}
        with unittest.mock.patch('mocking_example.solution.get_task', return_value=mock_value):
            daily_task = solution.my_daily_todo()
        self.assertEqual(daily_task, [{"userId": 1, "id": 1, "title": "delectus aut autem", "completed": False}])


if __name__ == "__main__":
    unittest.main()