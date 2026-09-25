"""Unit tests for ParkingTicket."""

import unittest
from parked_car import ParkedCar
from police_officer import PoliceOfficer
from parking_ticket import ParkingTicket


class TestParkingTicketInfo(unittest.TestCase):

    def setUp(self):
        self.car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 90)
        self.officer = PoliceOfficer("J. Smith", "4471")
        self.ticket = ParkingTicket(self.car, self.officer, 30)

    def test_car_info(self):
        self.assertEqual(self.ticket.make, "Honda")
        self.assertEqual(self.ticket.model, "Civic")
        self.assertEqual(self.ticket.color, "Blue")
        self.assertEqual(self.ticket.license_number, "ABC123")

    def test_officer_info(self):
        self.assertEqual(self.ticket.officer_name, "J. Smith")
        self.assertEqual(self.ticket.badge_number, "4471")

    def test_illegal_minutes(self):
        self.assertEqual(self.ticket.illegal_minutes, 30)


class TestParkingTicketFineBoundaries(unittest.TestCase):

    def setUp(self):
        self.car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 90)
        self.officer = PoliceOfficer("J. Smith", "4471")

    def test_one_minute_fine(self):
        ticket = ParkingTicket(self.car, self.officer, 1)
        self.assertEqual(ticket.fine, 25)

    def test_sixty_minutes_fine(self):
        ticket = ParkingTicket(self.car, self.officer, 60)
        self.assertEqual(ticket.fine, 25)

    def test_sixty_one_minutes_fine(self):
        ticket = ParkingTicket(self.car, self.officer, 61)
        self.assertEqual(ticket.fine, 35)

    def test_one_hundred_twenty_minutes_fine(self):
        ticket = ParkingTicket(self.car, self.officer, 120)
        self.assertEqual(ticket.fine, 35)

    def test_one_hundred_twenty_one_minutes_fine(self):
        ticket = ParkingTicket(self.car, self.officer, 121)
        self.assertEqual(ticket.fine, 45)


class TestParkingTicketReport(unittest.TestCase):

    def test_report_contains_required_info(self):
        car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 90)
        officer = PoliceOfficer("J. Smith", "4471")
        ticket = ParkingTicket(car, officer, 61)
        report = ticket.get_report()

        self.assertIn("Honda", report)
        self.assertIn("Civic", report)
        self.assertIn("Blue", report)
        self.assertIn("ABC123", report)
        self.assertIn("61", report)
        self.assertIn("35", report)
        self.assertIn("J. Smith", report)
        self.assertIn("4471", report)


class TestParkingTicketInvalidIllegalMinutes(unittest.TestCase):

    def setUp(self):
        self.car = ParkedCar("Honda", "Civic", "Blue", "ABC123", 90)
        self.officer = PoliceOfficer("J. Smith", "4471")

    def test_zero_illegal_minutes_raises_value_error(self):
        with self.assertRaises(ValueError):
            ParkingTicket(self.car, self.officer, 0)

    def test_negative_illegal_minutes_raises_value_error(self):
        with self.assertRaises(ValueError):
            ParkingTicket(self.car, self.officer, -5)

    def test_noninteger_illegal_minutes_raises_type_error(self):
        with self.assertRaises(TypeError):
            ParkingTicket(self.car, self.officer, 30.5)


if __name__ == "__main__":
    unittest.main()
