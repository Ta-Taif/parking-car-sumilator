
import unittest
from parking_meter import ParkingMeter


class TestParkingMeterConstruction(unittest.TestCase):

    def test_valid_construction(self):
        meter = ParkingMeter(60)
        self.assertEqual(meter.minutes_purchased, 60)


class TestParkingMeterMinutesPurchased(unittest.TestCase):

    def test_zero_minutes_purchased_is_valid(self):
        meter = ParkingMeter(0)
        self.assertEqual(meter.minutes_purchased, 0)

    def test_positive_minutes_purchased_is_valid(self):
        meter = ParkingMeter(120)
        self.assertEqual(meter.minutes_purchased, 120)

    def test_negative_minutes_purchased_raises_value_error(self):
        with self.assertRaises(ValueError):
            ParkingMeter(-5)

    def test_noninteger_minutes_purchased_raises_type_error(self):
        with self.assertRaises(TypeError):
            ParkingMeter(60.5)

    def test_string_minutes_purchased_raises_type_error(self):
        with self.assertRaises(TypeError):
            ParkingMeter("60")


class TestParkingMeterReassignment(unittest.TestCase):

    def test_reassign_minutes_purchased(self):
        meter = ParkingMeter(60)
        meter.minutes_purchased = 90
        self.assertEqual(meter.minutes_purchased, 90)

    def test_reassign_to_invalid_raises_value_error(self):
        meter = ParkingMeter(60)
        with self.assertRaises(ValueError):
            meter.minutes_purchased = -1


if __name__ == "__main__":
    unittest.main()
