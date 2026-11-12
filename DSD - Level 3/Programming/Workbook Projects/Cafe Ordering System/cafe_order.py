# Functions 
def display_menu():
    print("\n === MENU ===")
    print(f"1. Cheese pizza | Price: £{menu["cheese"]} (5% Discount!)")
    print(f"2. Pepperoni pizza | Price: £{menu["pepperoni"]} (10% Discount!)")
    print(f"3. Chicken pizza | Price: £{menu["chicken"]} (5% Discount!)")
    print(f"4. Pineapple pizza | Price: £{menu["pineapple"]} (10% Discount!)")
    print(f"5. Chocolate pizza | Price: £{menu["chocolate"]}")

def receipt(name, total, items, status):
    print("\n=== RECEIPT ===")
    print(f"Customer: {name}")
    print(f"Pizza(s) ordered: {items}")
    print(f"\n {status}")
    print(f"Purchase Total: £{total:.2f}")
    print("\n --- T H A N K  Y O U ---")

# Pizza menu with prices
menu = {
    "cheese": 8.99,
    "pepperoni": 14.99,
    "chicken": 6.99,
    "pineapple": 12.99,
    "chocolate": 4.99
}

# Welcoming the user, and collect their name
print("Welcome to the Pizza Café! What is your name?")
name = input("My name: ")

print(f"It's nice to see you {name}. What would you like to eat?")


ongoing_total = 0
ordering = True
items = 0


while ordering:

    display_menu()

    order = input("\n My order (1-5): ")

    if order == "1":
        item = "cheese pizza"
        price = menu["cheese"]
    elif order == "2":
        item = "pepperoni pizza"
        price = menu["pepperoni"]
    elif order == "3":
        item = "chicken pizza"
        price = menu["chicken"]
    elif order == "4":
        item = "pineapple pizza"
        price = menu["pineapple"]
    elif order == "5":
        item = "chocolate pizza"
        price = menu["chocolate"]
    else:
        item = "invalid"
        price = "invalid"

    print("")

    if item == "chocolate":
        print(f"You selected: {item}")
        print(f"Price: £{price}")
        print("What a strange choice!")
     
    elif item != "invalid":
        print(f"You selected: {item}")
        print(f"Price: £{price}")
    else:
        print("Invalid choice, please try again")

    if item != "invalid" and price != "invalid":

        quantity = int(input(f"How many {item} pizza(s) do you want. (min 1): "))
        ongoing_total += (price * quantity)
        items += (1 * quantity)
        total = ongoing_total
        
        print(f"Pizza ordered! Your total is: £{total:.2f}!")

        new_item = input("Enter (y/n) if you would like another pizza: ").lower()
        if new_item == "n":
            ordering = False
        elif new_item == "y":
            print("OK!")
        else:
            print("Invalid option, redirecting to checkout.")
            ordering = False

        print("")

if total >= 10:
    discount = total * 0.10
    total -= discount
    receipt(name, total, items, "Discount applied!")

elif total >= 5:
    discount = total * 0.05
    total -= discount

    receipt(name, total, items, "Discount applied!")
else:

    receipt(name, total, items, "")
