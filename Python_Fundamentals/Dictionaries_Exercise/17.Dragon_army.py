n = int(input())

dragons = {}
order_of_types = []  # to preserve input order

for _ in range(n):
    type_, name, damage, health, armor = input().split()

    # Replace null values
    damage = 45 if damage == "null" else int(damage)
    health = 250 if health == "null" else int(health)
    armor = 10 if armor == "null" else int(armor)

    if type_ not in dragons:
        dragons[type_] = {}
        order_of_types.append(type_)

    dragons[type_][name] = {"damage": damage, "health": health, "armor": armor}

# Output
for type_ in order_of_types:
    stats = dragons[type_]

    # Calculate averages
    avg_damage = sum(d["damage"] for d in stats.values()) / len(stats)
    avg_health = sum(d["health"] for d in stats.values()) / len(stats)
    avg_armor = sum(d["armor"] for d in stats.values()) / len(stats)

    print(f"{type_}::({avg_damage:.2f}/{avg_health:.2f}/{avg_armor:.2f})")

    # Print dragons sorted by name
    for name in sorted(stats.keys()):
        d = stats[name]
        print(f"-{name} -> damage: {d['damage']}, health: {d['health']}, armor: {d['armor']}")