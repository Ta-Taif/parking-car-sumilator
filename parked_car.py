

class ParkedCar:

    def __init__(self, make: str, model: str, color: str,
                 license_number: str, minutes_parked: int) -> None:

        self.make = make
        self.model = model
        self.color = color
        self.license_number = license_number
        self.minutes_parked = minutes_parked

    @property
    def make(self) -> str:
        return self._make

    @make.setter
    def make(self, value: str) -> None:
        self._make = self._validate_string(value, "make")

    @property
    def model(self) -> str:
        return self._model

    @model.setter
    def model(self, value: str) -> None:
        self._model = self._validate_string(value, "model")

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: str) -> None:
        self._color = self._validate_string(value, "color")

    @property
    def license_number(self) -> str:
        return self._license_number

    @license_number.setter
    def license_number(self, value: str) -> None:
        self._license_number = self._validate_string(value, "license_number")

    @property
    def minutes_parked(self) -> int:
        return self._minutes_parked

    @minutes_parked.setter
    def minutes_parked(self, value: int) -> None:
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("minutes_parked must be an int")
        if value < 0:
            raise ValueError("minutes_parked must be >= 0")
        self._minutes_parked = value

    @staticmethod
    def _validate_string(value: str, field_name: str) -> str:

        if not isinstance(value, str):
            raise TypeError(f"{field_name} must be a string")
        if not value.strip():
            raise ValueError(f"{field_name} must not be empty")
        return value
