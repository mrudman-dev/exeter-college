age = int(input("Enter your age: "))
is_weekend = input("Is it the weekend? (yes/no): ").lower() == "yes"

if age < 5:
    price = 0
else:
    if is_weekend:
        if age < 18:
            price = 8
        else:
            price = 12
    else:
        if age < 18:
            price = 6
        else:
            price = 10

print(f"Ticket price: £{price}")
