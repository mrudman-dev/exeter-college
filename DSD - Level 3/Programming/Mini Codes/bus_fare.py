# Match cases only

fare_stage = input("Please enter a fair stage: ").lower()

match fare_stage:
    case "town centre" | "station": price = 1.50
    case "college" | "retail park": price = 2
    case _: print("Unknown stage - please ask the driver")

print(f"Price : {price}")
