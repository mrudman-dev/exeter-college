# Restrictions
height_min = 90
age_min = 4

allowed_rides = ["Rollercoaster", "Ferris Wheel", "Drop Tower", "Teacups", "Supershot", "Train ride", "Flight of the pterosaur", "Horror Dropper"]

# Welcoming the user
print("============ // THEME PARK RIDE // ============")
print("Please enter the information below to verify that you can enter the rides.")


# Fetch the user's name, age, and height
print("\n - - - - - F O R M - - - - -")
name = input("[NAME] - ")
age = int(input("[AGE] - "))
height = int(input("[HEIGHT] - "))

print("\n ==== RIDES ====")

if age <= 4:

    removed_rides = ["Rollercoaster", "Ferris Wheel", "Drop Tower", "Supershot", "Horror Dropper"]
    rides_available = [item for item in allowed_rides if item not in removed_rides]

    print(f"Sorry! Since you are {age} years old, you only have {len(rides_available)} available rides.")
    print(f"Here are your available rides to choose: {rides_available}")

elif age > 4 and age <= 12:

    removed_rides = ["Rollercoaster", "Drop Tower", "Supershot", "Horror Dropper"]
    rides_available = [item for item in allowed_rides if item not in removed_rides]

    print(f"Since you are only {age} years old, we have automatically selected appropriate rides for you to choose!")
    print(f"Here are your available rides to choose: {rides_available}")

elif age >= 13 and age <= 17:

    removed_rides = ["Horror Drop", "Supershot"]
    rides_available = [item for item in allowed_rides if item not in removed_rides]

    print(f"Since you are {age} years old, we have removed some scary rides for you!")
    print(f"Here are your available appropriate rides for your age: {rides_available}")

elif age >= 18 and age <= 49:
    print(f"Here are your rides to choose: {allowed_rides}")

elif age >= 50:
    removed_rides = ["Rollercoaster", "Ferris Wheel", "Drop Tower", "Teacups", "Supershot", "Train ride", "Flight of the pterosaur", "Horror Dropper"]
    rides_available = [item for item in allowed_rides if item not in removed_rides]

    print("Sorry, we don't think these are suitable for your old age.")


print(rides_available)