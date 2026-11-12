print("=== WILDLIFE SIGHTING RECORDER ===") 
 
species = input("Animal species: ").strip() 
location = input("Reserve or location: ").strip() 


try:
    count = int(input("Number of animals seen: "))
    if count > 0:
        print(f"\n[SIGHTING SUMMARY]: Animal Species: {species} | Number of {species} seen: {count} | Location: {location}")
    else:
        print("\nPlease enter the sighting greater than 0")
        exit()
except ValueError:
    print("\nPlease use valid integer numbers only.")
    exit()


 
print("\nThank you for supporting wildlife conservation!") 