sightings = [] 
next_id = 1 
 
def add_sighting(): 
    global next_id 
    species = input("Species: ").strip() 
    location = input("Location: ").strip() 
    count = int(input("Number seen: ")) 

    if species != "" or location != "":
        if count > 0:
            new_sighting = {next_id, species, location, count}
            sightings.append(new_sighting)
            next_id += 1
        else:
            print("The number of species seen must be greater than 0.")
            return
    else:
        print("No empty inputs, please try again.")
        return
 
def view_sightings():

    num = 0

    if len(sightings) == 0:
        print("There are currently no sightings available to view.")
    else:
        for record in sightings:
            num += 1

            print(f"\n ==== SIGHTING No.{num} ==== \n")

            for key, value in record.items():
                print(key, "|", value)
 
def search_sightings(): 
    term = input("Species to search: ").strip().lower()
    
    term_record = next((record for record in sightings if record["species"] == term),None,)
    
    if term_record is None:
        print("\n No matches")
        return
    
    if len(sightings) > 0:
        for record in sightings:
            for key, value in record.items():
                print(key, "|", value)     
    else:
        print("No sightings available to display. Please add more.")    
 
def update_sighting(): 
    # TODO: Ask for a sighting ID. 
    # TODO: Find that ID and change its count. 
    # TODO: Report if the ID does not exist. 
    pass 
 
def delete_sighting(): 
    # TODO: Ask for a sighting ID. 
    # TODO: Confirm deletion before removing it. 
    pass 
 
while True: 
    print("\n1 Add  2 View  3 Search  4 Update  5 Delete  6 Exit") 
    choice = input("Choose: ") 
    if choice == "1": 
        add_sighting() 
    elif choice == "2": 
        view_sightings() 
    elif choice == "3": 
        search_sightings() 
    elif choice == "4": 
        update_sighting() 
    elif choice == "5": 
        delete_sighting() 
    elif choice == "6": 
        break 
    else: 
        print("Invalid menu choice")