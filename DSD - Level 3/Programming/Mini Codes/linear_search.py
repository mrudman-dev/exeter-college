found = False
index = 0

list = ["a", "b", "c", "d", "e", "f", "s", "g", "i", "3"]

while index < len(list) and found == False:
    if list[index] == "g":
        found = True
    else:
        index += 1

if found == True:
    print("Item found at position ", index)
else:
    print("Item not found")

