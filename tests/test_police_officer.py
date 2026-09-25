
import unittest
from parked_car import ParkedCar
from parking_meter import ParkingMeter
from parking_ticket import ParkingTicket
from police_officer import PoliceOfficer


class TestPoliceOfficerInspection(unittest.TestCase):

    def setUp(self):
        self.officer = PoliceOfficer("J. Smith", "4471")

    def test_parked_less_than_purchased_returns_none(self):
        car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 30)
        meter = ParkingMeter(60)
        result = self.officer.inspect_parking(car, meter)
        self.assertIsNone(result)

    def test_parked_exactly_as_long_as_purchased_returns_none(self):
        car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 60)
        meter = ParkingMeter(60)
        result = self.officer.inspect_parking(car, meter)
        self.assertIsNone(result)

    def test_parked_one_minute_too_long_returns_ticket(self):
        car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 61)
        meter = ParkingMeter(60)
        result = self.officer.inspect_parking(car, meter)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, ParkingTicket)


class TestPoliceOfficerIllegalMinutes(unittest.TestCase):

    def test_illegal_minutes_calculated_correctly(self):
        officer = PoliceOfficer("J. Smith", "4471")
        car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 95)
        meter = ParkingMeter(60)
        ticket = officer.inspect_parking(car, meter)
        self.assertEqual(ticket.illegal_minutes, 35)


class TestPoliceOfficerTicketInfo(unittest.TestCase):

    def test_ticket_contains_expected_info(self):
        officer = PoliceOfficer("J. Smith", "4471")
        car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 95)
        meter = ParkingMeter(60)
        ticket = officer.inspect_parking(car, meter)

        self.assertEqual(ticket.make, "Honda")
        self.assertEqual(ticket.license_number, "ABC123")
        self.assertEqual(ticket.officer_name, "J. Smith")
        self.assertEqual(ticket.badge_number, "4471")


class TestPoliceOfficerConstruction(unittest.TestCase):

    def test_valid_construction(self):
        officer = PoliceOfficer("J. Smith", "4471")
        self.assertEqual(officer.name, "J. Smith")
        self.assertEqual(officer.badge_number, "4471")

    def test_empty_name_raises_value_error(self):
        with self.assertRaises(ValueError):
            PoliceOfficer("", "4471")

    def test_non_string_badge_raises_type_error(self):
        with self.assertRaises(TypeError):
            PoliceOfficer("J. Smith", 4471)


if __name__ == "__main__":
    unittest.main()
