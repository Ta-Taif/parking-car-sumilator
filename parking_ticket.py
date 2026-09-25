
import math


class ParkingTicket:

    FIRST_HOUR_FINE = 25
    ADDITIONAL_HOUR_FINE = 10

    def __init__(self, car: "ParkedCar", officer: "PoliceOfficer",
                 illegal_minutes: int) -> None:

        self._car = car
        self._officer = officer
        self.illegal_minutes = illegal_minutes

    @property
    def illegal_minutes(self) -> int:
        return self._illegal_minutes

    @illegal_minutes.setter
    def illegal_minutes(self, value: int) -> None:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("illegal_minutes must be an int")
        if value <= 0:
            raise ValueError("illegal_minutes must be > 0 for a valid ticket")
        self._illegal_minutes = value

    @property
    def make(self) -> str:
        """str: The cited car's make."""
        return self._car.make

    @property
    def model(self) -> str:
        return self._car.model

    @property
    def color(self) -> str:
        return self._car.color

    @property
    def license_number(self) -> str:
        return self._car.license_number

    @property
    def officer_name(self) -> str:
        return self._officer.name

    @property
    def badge_number(self) -> str:
        return self._officer.badge_number

    @property
    def fine(self) -> int:

        hours = math.ceil(self._illegal_minutes / 60)
        return self.FIRST_HOUR_FINE + self.ADDITIONAL_HOUR_FINE * (hours - 1)

    def get_report(self) -> str:

        return (
            "PARKING TICKET\n"
            f"Car: {self.color} {self.make} {self.model}\n"
            f"License: {self.license_number}\n"
            f"Illegally parked for: {self.illegal_minutes} minutes\n"
            f"Fine: ${self.fine}\n"
            f"Issuing Officer: {self.officer_name} (Badge #{self.badge_number})"
        )
