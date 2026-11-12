FILE_NAME = "sightings.txt" 
 
def save_sightings(): 
    # TODO: Open FILE_NAME in write mode. 
    # TODO: For each record, write id|species|location|count. 
    # TODO: End every record with a newline. 
    pass 
 
def load_sightings(): 
    loaded = [] 
    try: 
        with open(FILE_NAME, "r", encoding="utf-8") as file: 
            for line in file: 
                parts = line.strip().split("|") 
                if len(parts) == 4: 
                    # TODO: Convert id and count to integers. 
                    # TODO: Create and append a dictionary. 
                    pass 
    except FileNotFoundError: 
        return [] 
    return loaded 
 
def conservation_report(): 
    # TODO: Count the number of sighting records. 
    # TODO: Calculate the total animals observed. 
    # TODO: Total observations for each species. 
    # TODO: Display the most-observed species. 
    pass