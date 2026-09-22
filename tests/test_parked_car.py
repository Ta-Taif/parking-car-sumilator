"""Unit tests for ParkedCar."""

import unittest
from parked_car import ParkedCar


class TestParkedCarConstruction(unittest.TestCase):
    """Valid construction and property access."""

    def test_valid_construction(self):
        # Arrange / Act
        car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 45)
        # Assert
        self.assertEqual(car.make, "Honda")
        self.assertEqual(car.model, "Civic")
        self.assertEqual(car.color, "Blue")
        self.assertEqual(car.license_number, "ABC123")
        self.assertEqual(car.minutes_parked, 45)


class TestParkedCarReassignment(unittest.TestCase):
    """Valid property reassignment."""

    def test_reassign_make(self):
        car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 45)
        car.make = "Toyota"
        self.assertEqual(car.make, "Toyota")

    def test_reassign_minutes_parked(self):
        car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 45)
        car.minutes_parked = 90
        self.assertEqual(car.minutes_parked, 90)


class TestParkedCarInvalidStrings(unittest.TestCase):
    """Empty or incorrect string values."""

    def test_empty_make_raises_value_error(self):
        with self.assertRaises(ValueError):
            ParkedCar("", "Civic", "Blue", "ABC123", 45)

    def test_whitespace_only_model_raises_value_error(self):
        with self.assertRaises(ValueError):
            ParkedCar("Honda", "   ", "Blue", "ABC123", 45)

    def test_non_string_color_raises_type_error(self):
        with self.assertRaises(TypeError):
            ParkedCar("Honda", "Civic", 5, "ABC123", 45)

    def test_non_string_license_raises_type_error(self):
        with self.assertRaises(TypeError):
            ParkedCar("Honda", "Civic", "Blue", 123, 45)


class TestParkedCarMinutesParked(unittest.TestCase):
    """Zero, positive, negative, and noninteger minutes parked."""

    def test_zero_minutes_parked_is_valid(self):
        car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 0)
        self.assertEqual(car.minutes_parked, 0)

    def test_positive_minutes_parked_is_valid(self):
        car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 120)
        self.assertEqual(car.minutes_parked, 120)

    def test_negative_minutes_parked_raises_value_error(self):
        with self.assertRaises(ValueError):
            ParkedCar("Honda", "Civic", "Blue", "ABC123", -1)

    def test_noninteger_minutes_parked_raises_type_error(self):
        with self.assertRaises(TypeError):
            ParkedCar("Honda", "Civic", "Blue", "ABC123", 45.5)

    def test_string_minutes_parked_raises_type_error(self):
        with self.assertRaises(TypeError):
            ParkedCar("Honda", "Civic", "Blue", "ABC123", "45")


if __name__ == "__main__":
    unittest.main()
