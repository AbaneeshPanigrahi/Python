# Custom Exceptions
class SeatNotAvailableError(Exception):
    pass

class InvalidPassengerError(Exception):
    pass

class PaymentFailureError(Exception):
    pass


class FlightBooking:

    def __init__(self):
        self.flights = {}
        self.bookings = []

    def add_flight(self):
        try:
            fid = int(input("Enter Flight ID: "))
            route = input("Enter route (e.g. Delhi -> Mumbai): ")
            seats = int(input("Enter number of seats: "))
            price = float(input("Enter ticket price: "))

            if fid in self.flights:
                print("Flight ID already exists!")
                return

            self.flights[fid] = {
                "route": route,
                "seats": seats,
                "price": price
            }

            print("Flight added successfully!")

        except ValueError:
            print("Invalid input!")

    def search_flights(self):
        print("\nAvailable Flights")
        for fid, details in self.flights.items():
            print(fid, "-", details["route"], "| Seats:", details["seats"], "| Price:", details["price"])

    def book_ticket(self):
        try:
            self.search_flights()

            fid = int(input("Enter flight ID: "))
            name = input("Enter passenger name: ")
            payment = input("Enter payment method (card/upi): ")

            if name.strip() == "":
                raise InvalidPassengerError("Invalid passenger details!")

            if fid not in self.flights:
                raise InvalidPassengerError("Invalid flight ID!")

            if self.flights[fid]["seats"] <= 0:
                raise SeatNotAvailableError("No seats available!")

            if payment not in ["card", "upi"]:
                raise PaymentFailureError("Payment failed! Invalid method.")

            self.flights[fid]["seats"] -= 1
            self.bookings.append({"name": name, "flight": fid})

            print("Ticket booked successfully!")

        except (SeatNotAvailableError, InvalidPassengerError, PaymentFailureError) as e:
            print("Error:", e)

        except ValueError:
            print("Invalid input!")

    def cancel_ticket(self):
        name = input("Enter passenger name to cancel ticket: ")

        for booking in self.bookings:
            if booking["name"] == name:
                fid = booking["flight"]
                self.flights[fid]["seats"] += 1
                self.bookings.remove(booking)
                print("Ticket cancelled successfully!")
                return

        print("Booking not found!")


system = FlightBooking()

while True:
    print("\n--- Flight Booking System ---")
    print("1. Add Flight")
    print("2. Search Flights")
    print("3. Book Ticket")
    print("4. Cancel Ticket")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            system.add_flight()

        elif choice == 2:
            system.search_flights()

        elif choice == 3:
            system.book_ticket()

        elif choice == 4:
            system.cancel_ticket()

        elif choice == 5:
            print("Exiting system")
            break

        else:
            print("Invalid choice!")

    except ValueError:
        print("Enter a valid number!")