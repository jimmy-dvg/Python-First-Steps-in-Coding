animals = {}
areas = {}

while True:
    line = input()

    if line == "EndDay":
        break

    elif line.startswith("Add:"):
        parts = line[5:].split("-")
        animal_name = parts[0]
        needed_food = int(parts[1])
        area = parts[2]

        if animal_name in animals:
            animals[animal_name] += needed_food
        else:
            animals[animal_name] = needed_food
            if area not in areas:
                areas[area] = []
            areas[area].append(animal_name)

    elif line.startswith("Feed:"):
        parts = line[6:].split("-")
        animal_name = parts[0]
        food = int(parts[1])

        if animal_name not in animals:
            continue

        animals[animal_name] -= food

        if animals[animal_name] <= 0:
            print(f"{animal_name} was successfully fed")
            del animals[animal_name]
            for area in areas:
                if animal_name in areas[area]:
                    areas[area].remove(animal_name)
                    break

print("Animals:")
for animal, food in animals.items():
    print(f"  {animal} -> {food}g")

print("Areas with hungry animals:")
for area, animal_list in areas.items():
    hungry_count = len(animal_list)
    if hungry_count > 0:
        print(f"  {area}: {hungry_count}")
