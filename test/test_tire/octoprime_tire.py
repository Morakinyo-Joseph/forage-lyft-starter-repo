import unittest
from tires.octoprime_tire import OctoprimeTire


class TestOctoprimeTire(unittest.TestCase):
    def test_needs_service_true(self):
        tire_wear = [0.1, 0.3, 0.8, 0.8]
        tire = OctoprimeTire(tire_wear)
        self.assertTrue(tire.needs_service())

    def test_needs_service_false(self):
        tire_wear = [0.2, 0.3, 0.4, 0.5]
        tire = OctoprimeTire(tire_wear)
        self.assertFalse(tire.needs_service())
