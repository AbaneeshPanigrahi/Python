# Parking Lot Management System

class ParkingLot:
    def __init__(self):
        self.total_spots = 50
        self.occupied_spots = 0
        self.fee_per_hour = 20

    def vehicle_entry(self):
        if self.occupied_spots < self.total_spots:
            self.occupied_spots += 1
            print("Vehicle entered the parking lot")
        else:
            print("Parking lot is full")

    def vehicle_exit(self, hours):
        if self.occupied_spots > 0:
            self.occupied_spots -= 1
            fee = hours * self.fee_per_hour
            print("Vehicle exited")
            print("Parking fee:", fee)
        else:
            print("No vehicles in parking lot")

    def available_spots(self):
        available = self.total_spots - self.occupied_spots
        print("Available spots:", available)


parking = ParkingLot()

while True:
    print("\n--- Parking Lot Menu ---")
    print("1. Vehicle Entry")
    print("2. Vehicle Exit")
    print("3. Check Available Spots")
    print("4. Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        parking.vehicle_entry()

    elif choice == 2:
        hours = int(input("Enter parking hours: "))
        parking.vehicle_exit(hours)

    elif choice == 3:
        parking.available_spots()

    elif choice == 4:
        print("System Closed")
        break

    else:
        print("Invalid Choice")