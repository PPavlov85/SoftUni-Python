import unittest

from project.survivor import Survivor


class TestSurvivor(unittest.TestCase):

    def test_set_attr(self):
        s = Survivor("test", 10)
        self.assertEqual(s.name, "test")
        self.assertEqual(s.age, 10)
        self.assertEqual(s.health, 100)
        self.assertEqual(s.needs, 100)
        self.assertEqual(s.needs_healing, False)
        self.assertEqual(s.needs_sustenance, False)

    def test_name_error(self):
        with self.assertRaises(ValueError) as ex:
            s = Survivor("", 10)
        self.assertEqual(str(ex.exception), "Name not valid!")

    def test_age_error(self):
        with self.assertRaises(ValueError) as ex:
            s = Survivor("test", -10)
        self.assertEqual(str(ex.exception), "Age not valid!")

    def test_health_error(self):
        s = Survivor("test", 10)
        with self.assertRaises(ValueError) as ex:
            s.health = -10
        self.assertEqual(str(ex.exception), "Health not valid!")

    def test_health_more_than_100(self):
        s = Survivor("test", 10)
        s.health -= 10
        s.health += 20
        self.assertEqual(s.health, 100)

    def test_needs_error(self):
        s = Survivor("test", 10)
        with self.assertRaises(ValueError) as ex:
            s.needs = -10
        self.assertEqual(str(ex.exception), "Needs not valid!")

    def test_need_more_than_100(self):
        s = Survivor("test", 10)
        s.needs -= 10
        s.needs += 20
        self.assertEqual(s.needs, 100)

    def test_needs_sustenance(self):
        s = Survivor("test", 10)
        s.needs -= 10
        self.assertEqual(s.needs_sustenance, True)

    def test_needs_healing(self):
        s = Survivor("test", 10)
        s.health -= 10
        self.assertEqual(s.needs_healing, True)
