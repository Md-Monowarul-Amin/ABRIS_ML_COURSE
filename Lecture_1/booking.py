TOTAL_TICKETS = 50
available_tickets = 50

def get_user_input():
    full_name = input("Enter your full name: ")
    email = input("Enter your email address: ")
    number_of_tickets = int(input("Enter number of tickets you want to book: "))
    return full_name, email, number_of_tickets

def is_available(user_tickets):
    if user_tickets <= available_tickets:
        return True

def is_input_valid(full_name, email:str, user_tickets):
    if len(full_name) < 3:
        print("Your name must me more than 3 characters.")
        return False
    if "@" not in email:
        print("Not valid email")
        return False
    if not is_available(user_tickets):
        print(user_tickets, "Tickets Not Available ", " Only ", available_tickets, " Tickets Remaining. ")
        return False
    return True

def split_name(full_name:str):
    splitted_name = full_name.split(" ")
    first_name = splitted_name[0]
    last_name = splitted_name[1]
    return first_name, last_name

def book_ticket(full_name, user_tickets, email, all_bookings:list):
    global available_tickets
    available_tickets -= user_tickets  ## available_tickets = available_tickets - user_tickets
    first_name, last_name = split_name(full_name)

    booking_dict = dict()
    booking_dict["first_name"] = first_name
    booking_dict["last_name"] = last_name
    booking_dict["email"] = email
    booking_dict["user_ticket"] = user_tickets

    all_bookings.append(booking_dict)


def print_bookings(all_bookings:list):
    for i in range(len(all_bookings)):
        print(all_bookings[i])
    print(available_tickets, " Tickets Remaining.")

all_bookings = []

while available_tickets > 0:
    full_name, email, user_tickets = get_user_input()
    if is_input_valid(full_name, email, user_tickets):
        book_ticket(full_name, user_tickets, email, all_bookings)
        print_bookings(all_bookings)
    else:
        continue



