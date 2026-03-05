dwarfs = {}

while True:
    line = input()
    if line == "Once upon a time":
        break

    name, color, physics = line.split(" <:> ")
    physics = int(physics)

    key = (name, color)

    if key not in dwarfs:
        dwarfs[key] = physics
    else:
        if dwarfs[key] < physics:
            dwarfs[key] = physics

# Count dwarfs per color
color_count = {}
for (name, color), phys in dwarfs.items():
    if color not in color_count:
        color_count[color] = 0
    color_count[color] += 1

# Sort dwarfs
sorted_dwarfs = sorted(
    dwarfs.items(),
    key=lambda item: (-item[1], -color_count[item[0][1]])
)

# Print result
for (name, color), physics in sorted_dwarfs:
    print(f"({color}) {name} <-> {physics}")