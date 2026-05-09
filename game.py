rooms = {
    "Living Room": {"north": "Kitchen", "item": "Key"},
    "Kitchen": {"south": "Living Room", "east": "Bedroom"},
    "Bedroom": {"west": "Kitchen"}
}

current_room = "Living Room"
inventory = []

while True:
    print("\n---------------------------")
    print(f"You are in the {current_room}")
    print("---------------------------")
    print(f"Inventory: {inventory}")

    if "item" in rooms[current_room]:
        item = rooms[current_room]["item"]
        print(f"You see a {item}")

    move = input("Move (north/south/east/west) or 'get item': ").lower()

    if move == "get item":
        if "item" in rooms[current_room]:
            item = rooms[current_room]["item"]
            inventory.append(item)
            print(f"{item} added to inventory!")
            del rooms[current_room]["item"]
        else:
            print("No item here.")

    elif move in rooms[current_room]:
        current_room = rooms[current_room][move]

    else:
        print("Invalid move.")

    if current_room == "Bedroom" and "Key" in inventory:
        print("You unlocked the room and won the game!")
        break

    if current_room == "Bedroom" and "Key" not in inventory:
        print("You entered without the key. You lose!")
        break
