rooms = {
    "Living Room": {"north": "Kitchen", "item": "Key"},
    "Kitchen": {"south": "Living Room", "east": "Bedroom"},
    "Bedroom": {"west": "Kitchen", "item": "Sword"}
}

current_room = "Living Room"
inventory = []

while True:
    print(f"\nYou are in the {current_room}")
    
    if "item" in rooms[current_room]:
        item = rooms[current_room]["item"]
        print(f"You see a {item}")
    
    move = input("Move (north/south/east/west) or 'get item': ").lower()
    
    if move == "get item":
        if "item" in rooms[current_room]:
            inventory.append(item)
            print(f"{item} added to inventory!")
            del rooms[current_room]["item"]
        else:
            print("No item here.")
    
    elif move in rooms[current_room]:
        current_room = rooms[current_room][move]
    else:
        print("Invalid move.")
