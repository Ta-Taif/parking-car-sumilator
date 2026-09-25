

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from parking_ticket import ParkingTicket


class PoliceOfficer:

    def __init__(self, name: str, badge_number: str) -> None:

        self.name = name
        self.badge_number = badge_number

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str) -> None:
        self._name = self._validate_string(value, "name")

    @property
    def badge_number(self) -> str:
        return self._badge_number

    @badge_number.setter
    def badge_number(self, value: str) -> None:
        self._badge_number = self._validate_string(value, "badge_number")

    @staticmethod
    def _validate_string(value: str, field_name: str) -> str:
        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        if not value.strip():
            raise ValueError(f"{field_name} must not be empty")
        return value

    def inspect_parking(self, car: ParkedCar, meter: ParkingMeter):

        illegal_minutes = car.minutes_parked - meter.minutes_purchased
        if illegal_minutes <= 0:
            return None
        return ParkingTicket(car, self, illegal_minutes)
