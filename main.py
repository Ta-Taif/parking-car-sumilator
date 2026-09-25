"""main.py

Demonstrates the parking ticket simulator: one car within its
purchased time (no ticket), and one car that has overstayed its
purchased time (a ticket is issued and reported).
"""

from parked_car import ParkedCar
from parking_meter import ParkingMeter
from police_officer import PoliceOfficer


def main():
    officer = PoliceOfficer("J. Smith", "4471")

    print("Case 1: Car within purchased time")
    car1 = ParkedCar("Honda", "Civic", "Blue", "ABC123", 45)
    meter1 = ParkingMeter(60)
    ticket1 = officer.inspect_parking(car1, meter1)
    if ticket1 is None:
        print("No violation. No ticket issued.\n")
    else:
        print(ticket1.get_report(), "\n")

    print("Case 2: Car that overstayed its purchased time")
    car2 = ParkedCar("Toyota", "Corolla", "Red", "XYZ789", 95)
    meter2 = ParkingMeter(60)
    ticket2 = officer.inspect_parking(car2, meter2)
    if ticket2 is None:
        print("No violation. No ticket issued.")
    else:
        print(ticket2.get_report())


if __name__ == "__main__":
    main()
