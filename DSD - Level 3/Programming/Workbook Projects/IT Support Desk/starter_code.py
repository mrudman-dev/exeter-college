# ==========================================
# IT HELPDESK TICKET SYSTEM
# Intermediate Python Challenge
# ==========================================

tickets = []
ticket_number = 1000


def display_menu():
    print("\n==============================")
    print("      IT HELPDESK SYSTEM")
    print("==============================")
    print("1. Create a new ticket")
    print("2. View all tickets")
    print("3. Search for a ticket")
    print("4. View ticket statistics")
    print("5. Exit")
    print("==============================")


def create_ticket():
    global ticket_number

    print("\n--- CREATE NEW TICKET ---")
    name = input("Enter your name: ")
    issue = input("Describe the problem: ")

    print("\n Priority:")
    print("1. Low")
    print("2. Medium")
    print("3. High")
    priority_choice = input("Choose priority (1-3): ")

    # TODO 1:
    # Convert the priority choice into Low, Medium or High.

    if priority_choice == "1":
        priority = "Low"
    elif priority_choice == "2":
        priority = "Medium"
    elif priority_choice == "3":
        priority = "High"

    ticket = {
        "ticket_number": ticket_number,
        "name": name,
        "issue": issue,
        "priority": priority,
        "status": "Open"
    }

    # TODO 2:
    # Add the ticket to the tickets list.
    tickets.append(ticket)

    print("\n Ticket created successfully!")
    print("Your ticket number is:", ticket_number)


def view_tickets():
    print("\n--- ALL TICKETS ---")

    # TODO 3:
    # If there are no tickets, display "No tickets found."
    # Otherwise loop through the list and display each ticket clearly.

    num = 0
    
    if len(tickets) > 0:
            for record in tickets:
                num +=1

                print(f"\n ==== TICKET No. {num} ==== \n")
                    
                for key, value in record.items():
                    print(key, "|", value)
    else:
        print("No tickets found.")

def search_ticket():
    print("\n--- SEARCH TICKETS ---")
    search_number = int(input("Enter ticket number: "))

    # TODO 4:
    # Search for the requested ticket.
    # Display it if found.
    # Display an appropriate message if it is not found.

    if len(tickets) > 0 and 0 <= search_number < len(tickets):

        record = tickets[search_number]
        print(f"==== TICKET No. {search_number} ==== ")

        for key, value in record.items():
            print(key, "|", value)
    else:
        print(f"No ticket No.{search_number} is found in our database.")   
 

def ticket_statistics():
    print("\n--- TICKET STATISTICS ---")

    # TODO 5:
    # Display:
    # - total tickets
    # - Low priority tickets
    # - Medium priority tickets
    # - High priority tickets

    low_tickets = 0
    medium_tickets = 0
    high_tickets = 0

    print(f"\n Total number of tickets: {len(tickets)}")

    if len(tickets) > 0:
        for record in tickets:     
            for key, value in record.items():
                if key == "priority":
                    if value == "Low":
                        low_tickets += 1
                    elif value == "Medium":
                        medium_tickets += 1
                    elif value == "High":
                        high_tickets += 1
    else:
        low_tickets = 0
        medium_tickets = 0
        high_tickets = 0

    print(f"Low prority tickets: {low_tickets}")
    print(f"Medium prority tickets: {medium_tickets}")
    print(f"High prority tickets: {high_tickets}")

    HighProrityPercentage = (high_tickets / len(tickets)) * 100

    print(f"Percentage of high prority tickets: {HighProrityPercentage:.1f}%")

# ==========================================
# MAIN PROGRAM
# ==========================================

running = True

while running:
    display_menu()
    choice = input("\nChoose an option: ")

    if choice == "1":
        create_ticket()
    elif choice == "2":
        view_tickets()
    elif choice == "3":
        search_ticket()
    elif choice == "4":
        ticket_statistics()
    elif choice == "5":
        print("\nClosing IT Helpdesk System...")
        running = False
    else:
        print("\nInvalid option. Please try again.")
