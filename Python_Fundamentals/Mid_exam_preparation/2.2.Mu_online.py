rooms = input().split("|")
health = 100
bitcoins = 0
best_room = 0
you_have_died = False
for room in rooms:
    best_room += 1
    room = room.split()
    command, number = room[0], int(room[1])
    if command == "potion":
        initial_health = health
        health += number
        if health > 100:
            health = 100
        amount = health - initial_health
        print(f"You healed for {amount} hp.")
        print(f"Current health: {health} hp.")
    elif command == "chest":
        bitcoins += number
        print(f"You found {number} bitcoins.")
    # Monster
    else:
        health -= number
        if health > 0:
            print(f"You slayed {command}.")
        else:
            you_have_died = True
            break
if you_have_died:
    print(f"You died! Killed by {command}.")
    print(f"Best room: {best_room}")
else:
    print("You've made it!")
    print(f"Bitcoins: {bitcoins}")
    print(f"Health: {health}")
