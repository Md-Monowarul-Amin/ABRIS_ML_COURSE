TOTAL_TICKETS = 50 
available_tickets = 50

booking_list = []

def take_user_input():
    user_name = input("Please enter your full name: ")
    email = input("Enter your email: ")
    user_tickets = int(input("Enter number of tickets: "))

    return user_name, email, user_tickets

def is_valid_input():
    if user_tickets > available_tickets:
        print("Only", available_tickets, "tickets available")
        return False

    if "@" not in email:
        print("Not a valid email")
        return False
    
    return True

def book_ticket(user_name, email, user_tickets):
    global available_tickets
    available_tickets = available_tickets - user_tickets
    booking_dict = dict()
    booking_dict["user_name"] = user_name
    booking_dict["email"] = email
    booking_dict["user_tickets"] = user_tickets

    booking_list.append(booking_dict)

def print_bookings():
    # for i in range(len(booking_list)):
    #     print(booking_list[i])
    for booking in booking_list:
        print(booking)

while available_tickets > 0:

    user_name, email, user_tickets = take_user_input()

    if is_valid_input():
        book_ticket(user_name, email, user_tickets)
    else:
        continue

    # if available_tickets == 0:
    #     break


print_bookings()


# print("Now", available_tickets, "are available")
# # print(f"Now{available_tickets}are available")
# print("Booking list: ", booking_list)

first_name = user_name.split(" ")

# print(user_name,"with email", email, "Booked ", user_tickets, "tickets")