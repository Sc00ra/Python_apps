class CinemaError(Exception):
    pass

class NoSeatsAvailable(CinemaError):
    pass

class SeatAlreadyReserved(CinemaError):
    pass

class DuplicateReservation(CinemaError):
    pass

class ReservationNotFound(CinemaError):
    pass

# Inicjalizacja miejsc w kinie
def initialize_seats(rows, cols):
    return {(chr(65 + i), j+1): None for i in range(rows) for j in range(cols)}

# Rezerwacja miejsca
def reserve_seat(seats, user_reservations, row, col, user):
    if all(seat is not None for seat in seats.values()):
        raise NoSeatsAvailable("No seats available for the show.")
    
    if seats[(row, col)] is not None:
        raise SeatAlreadyReserved(f"Seat {row}{col} is already reserved.")
    
    if user in user_reservations:
        raise DuplicateReservation(f"User {user} has already reserved a seat.")
    
    seats[(row, col)] = user
    user_reservations[user] = (row, col)
    print(f"Seat {row}{col} has been reserved for {user}.")

# Anulowanie rezerwacji
def cancel_reservation(seats, user_reservations, row, col, user):
    if seats[(row, col)] == user:
        seats[(row, col)] = None
        del user_reservations[user]
        print(f"Reservation for seat {row}{col} by {user} has been cancelled.")
    else:
        raise ReservationNotFound(f"No reservation found for seat {row}{col} by {user}.")

# Przykład użycia
seats = initialize_seats(5, 5)  # 5x5 kino
user_reservations = {}

try:
    reserve_seat(seats, user_reservations, 'A', 2, "Wiktor Salvatti")
    reserve_seat(seats, user_reservations, 'A', 2, "Szymon Trojan") 
except CinemaError as e:
    print(e)

try:
    reserve_seat(seats, user_reservations, 'B', 3, "Łukaszenko firek")  
except CinemaError as e:
    print(e)

try:
    cancel_reservation(seats, user_reservations, 'A', 2, "Wojtek Sut") 
except CinemaError as e:
    print(e)

try:
    cancel_reservation(seats, user_reservations, 'A', 2, "Piter Farmazon")
except CinemaError as e:
    print(e)

try:
    reserve_seat(seats, user_reservations, 'B', 4, "Falafel")
except CinemaError as e:
    print(e)

# Sprawdzenie dostępnych miejsc
print("Available seats:")
for seat, user in seats.items():
    if user is None:
        print(f"Seat {seat[0]}{seat[1]} is available.")