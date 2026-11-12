 
import random 
import json 
from pathlib import Path 


# THE LOST TEMPLE - BEGINNER 
print("=== THE LOST TEMPLE ===") 
name = input("What is your name, explorer? ") 
print(f"Welcome, {name}! You stand at the temple entrance.") 
 
print("\n1. Enter the dark corridor") 
print("2. Explore the courtyard") 
choice = input("Choose 1 or 2: ").strip() 
 
if choice == "1": 
    print("You enter the dark corridor.") 

    stone_door = input("Open the stone door? [Y/N]: ").upper()
    if stone_door == "Y":
        print("Stone door opens")
    else:
        print("The stone door remains closed.")

elif choice == "2": 
    print("You find an overgrown courtyard.")

    climb_tower = input("Climb the tower? [Y/N]: ").upper()
    if climb_tower == "Y":
        print("You climb the tower.")
    else:
        print("You walk past the tower.")
else: 
    print("That is not a valid route.") 
 
print("You've completed the first set of the story! Moving on.")

# THE LOST TEMPLE - INTERMEDIATE 
rooms = { 
    "entrance": { 
        "description": "You are at the temple entrance.", 
        "exits": {"north": "hall"}, 
        "item": None 
    }, 
    "hall": { 
        "description": "Torches flicker along a long hall.", 
        "exits": {"south": "entrance", "east": "vault"}, 
        "item": "bronze key" 
    }, 
    "vault": { 
        "description": "A sealed chest stands in the vault.", 
        "exits": {"west": "hall"}, 
        "item": "treasure" 
    } 
} 
 
current_room = "entrance" 
inventory = [] 
running = True 
 
def show_room(): 
    room = rooms[current_room] 
    print("\n" + room["description"]) 
    print("Exits:", ", ".join(room["exits"])) 
    print("Item:", room["item"] or "none") 
 
while running:
    room = rooms[current_room] 

    show_room() 
    command = input("\nMove (direction), take, bag or quit: ").lower().strip() 
 
    if command == "quit": 
        running = False 
 
    elif command == "bag": 
        print("Inventory:", inventory) 
 
    elif command == "take": 
        if rooms[current_room]["item"] == None:
            inventory.append(room["item"])
            room["item"] = None
            print("No items found in the", rooms[current_room])
        else:
            inventory.append(room["item"])
            room["item"] = None
 
    elif command in rooms[current_room]["exits"]: 
        next_room = rooms[current_room]["exits"][command] 

        if "bronze key" in inventory:
            print("Bronze Key found in your inventory, entering the vault!")
        else:
            current_room = next_room
    else: 
        print("Unknown command.") 
 
if "treasure" in inventory:
    print("Congratulations! You have found the treasure. Please proceed.")
 
SAVE_FILE = Path("temple_save.json") 
health = 100 
 
def encounter(): 
    global health 
    # TODO 1: Use random.randint(1, 3). 
    # On one result, reduce health by 15. 
    # On other results, display a safe outcome. 
    pass 
 
def save_game(): 
    data = { 
        "room": current_room, 
        "inventory": inventory, 
        "health": health, 
        "rooms": rooms 
    } 
    # TODO 2: Write data to SAVE_FILE using 
    # json.dump(data, file, indent=2). 
    pass 
 
def load_game(): 
    global current_room, inventory, health, rooms 
    # TODO 3: Check whether SAVE_FILE exists. 
    # TODO 4: Read JSON with json.load(file). 
    # TODO 5: Restore the four game variables. 
    # TODO 6: Handle missing/invalid save files. 
    pass 
 
# TODO 7: Add "save" and "load" commands to your loop. 
# TODO 8: Call encounter() when entering a new room. 
# TODO 9: End the game when health <= 0. 