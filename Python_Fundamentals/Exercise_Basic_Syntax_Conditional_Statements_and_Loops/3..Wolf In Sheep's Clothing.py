animals = input().split(", ")

wolf_index = animals.index("wolf")
sheep_number = len(animals) - 1 - wolf_index

if sheep_number == 0:
    print("Please go away and stop eating my sheep")
else:
    print(f"Oi! Sheep number {sheep_number}! You are about to be eaten by a wolf!")
