import unittest
from project.hardware.hardware import Hardware
from project.software.software import Software


class TestHardware(unittest.TestCase):
    def setUp(self) -> None:
        self.hrd = Hardware("HDD", "Heavy", 1000, 200)

    def test_attributes(self):
        self.assertEqual(self.hrd.name, "HDD")
        self.assertEqual(self.hrd.type, "Heavy")
        self.assertEqual(self.hrd.capacity, 1000)
        self.assertEqual(self.hrd.memory, 200)
        self.assertEqual(len(self.hrd.software_components), 0)

    def test_can_be_crate_instance(self):
        Hardware("HDD", "Heavy", 1000, 200)

    def test_install_exception_not_enough_capacity(self):
        software = Software("Skype", "Express", 1001, 100)
        with self.assertRaises(Exception) as exc:
            self.hrd.install(software)
        self.assertEqual(str(exc.exception), "Software cannot be installed")

    def test_install_exception_not_enough_memory(self):
        software = Software("Skype", "Express", 500, 201)
        with self.assertRaises(Exception) as exc:
            self.hrd.install(software)
        self.assertEqual(str(exc.exception), "Software cannot be installed")

    def test_install_success(self):
        self.assertEqual(len(self.hrd.software_components), 0)
        software = Software("Skype", "Express", 200, 100)
        self.hrd.install(software)
        self.assertEqual(len(self.hrd.software_components), 1)

    def test_uninstall_success(self):
        self.assertEqual(len(self.hrd.software_components), 0)
        software = Software("Skype", "Express", 200, 100)
        self.hrd.install(software)
        self.hrd.uninstall(software)
        self.assertEqual(len(self.hrd.software_components), 0)


if __name__ == '__main__':
    unittest.main()
