#Movie Ticket Booking System
#Features:
#Movie name
#show times 
#check availability
#book ticket
#cancel ticket
# Movie Ticket Booking System

class MovieTicket:
    def __init__(self):
        self.movie_name = input("Enter movie name: ")
        self.show_time = input("Enter show time: ")
        self.total_seats = 100
        self.booked_seats = 0
        self.cancelled_seats = 0   


movie = MovieTicket()

while True:
    print("\n===== Movie Ticket Booking System =====")
    print("1. Show Movie Details")
    print("2. Check Availability")
    print("3. Book Ticket")
    print("4. Cancel Ticket")
    print("5. Booking/Cancel Details")
    print("6. Exit")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        print("Movie Name:", movie.movie_name)
        print("Show Time:", movie.show_time)

    elif choice == "2":
        available_seats = movie.total_seats - movie.booked_seats
        print("Available seats:", available_seats)

    elif choice == "3":
        seats = int(input("Enter number of tickets to book: "))
        if seats <= 0:
            print("Invalid number of seats.")
        elif movie.booked_seats + seats <= movie.total_seats:
            movie.booked_seats += seats
            print(seats, "tickets booked successfully.")
        else:
            print("Not enough seats available.")

    elif choice == "4":
        seats = int(input("Enter number of tickets to cancel: "))
        if seats <= 0:
            print("Invalid number of seats.")
        elif seats <= movie.booked_seats:
            movie.booked_seats -= seats
            movie.cancelled_seats += seats   
            print(seats, "tickets cancelled successfully.")
            print("Available Seats:", movie.total_seats - movie.booked_seats)
        else:
            print("Cannot cancel more tickets than booked.")

    elif choice == "5":
        print("Movie Name:", movie.movie_name)
        print("Show Time:", movie.show_time)
        print("Total Seats:", movie.total_seats)
        print("Booked Seats:", movie.booked_seats)
        print("Cancelled Seats:", movie.cancelled_seats)
        # print("Available Seats:", movie.total_seats - movie.booked_seats)

    elif choice == "6":
        print("Thank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")