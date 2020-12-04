from test_worker.solution import Worker
from parameterized import parameterized
import unittest


class WorkerTests(unittest.TestCase):
    def setUp(self) -> None:
        self.worker = Worker("Ivo", 100, 21)

    def test_worker_is_initialized(self):
        self.assertEqual(self.worker.name, "Ivo")
        self.assertEqual(self.worker.salary, 100)
        self.assertEqual(self.worker.energy, 21)

    def test_energy_is_increased_after_rest(self):
        old_energy = self.worker.energy
        self.worker.rest()
        self.assertEqual(self.worker.energy - old_energy, 1)

    @parameterized.expand([
        (-55, True),
        (-42, True),
        (-43, True),
        (0,   True),
        (5,   False),
        (9,   False),
        (10,   False),
    ])
    def test_worker_raises_exception_when_working_with_zero_energy(self, energy, should_raise):
        # for energy in (0, -42):
        #     self.worker.energy = energy
        #   self.worker.energy = 0
        #     with self.assertRaises(Exception):
        #         self.worker.work()
        self.worker.energy = energy
        if should_raise:
            with self.assertRaises(Exception):
                self.worker.work()
        else:
            self.worker.work()

    def test_worker_raises_exception_when_working_with_negative_energy(self):
        self.worker.energy = -42
        with self.assertRaises(Exception):
            self.worker.work()

    def test_worker_money_is_increased_after_work(self):
        old_money = self.worker.money
        self.worker.work()
        self.assertEqual(self.worker.money - old_money, self.worker.salary)

    def test_worker_energy_decreases_after_work(self):
        old_energy = self.worker.energy
        self.worker.work()
        self.assertEqual(self.worker.energy - old_energy, -1)

    def test_get_info(self):
        info = self.worker.get_info()
        self.assertEqual(info, f'{self.worker.name} has saved {self.worker.money} money.')


if __name__ == "__main__":
    unittest.main()
