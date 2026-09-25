
class ParkingMeter:
    """A parking meter with a validated minutes_purchased property."""

    def __init__(self, minutes_purchased: int) -> None:

        self.minutes_purchased = minutes_purchased

    @property
    def minutes_purchased(self) -> int:
        return self._minutes_purchased

    @minutes_purchased.setter
    def minutes_purchased(self, value: int) -> None:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("minutes_purchased must be an int")
        if value < 0:
            raise ValueError("minutes_purchased must be >= 0")
        self._minutes_purchased = value
