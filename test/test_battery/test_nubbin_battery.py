import unittest
from datetime import date

from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(unittest.TestCase):
    def test_needs_service_true(self):
        last_service_date = date.fromisoformat("2020-05-19")
        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        last_service_date = date.fromisoformat("2020-05-19")
        battery = NubbinBattery(last_service_date)
        self.assertTrue(battery.needs_service())