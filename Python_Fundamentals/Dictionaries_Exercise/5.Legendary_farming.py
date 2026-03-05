materials = {"shards": 0, "fragments": 0, "motes": 0}
legendary_item = ""
won_legendary_item = False
while not won_legendary_item:
    current_materials = input().split()
    for index in range(0, len(current_materials), 2):
        key = current_materials[index +1].lower()
        value = int(current_materials[index])
        if key not in materials.keys():
            materials[key] = 0
        materials[key] += value
        if materials["shards"] >= 250:
            legendary_item = "Shadowmourne"
            materials["shards"] -= 250
            won_legendary_item = True
        elif materials["fragments"] >= 250:
            legendary_item = "Valanyr"
            materials["fragments"] -= 250
            won_legendary_item = True
        elif materials["motes"] >= 250:
            legendary_item = "Dragonwrath"
            materials["motes"] -= 250
            won_legendary_item = True
        if won_legendary_item:
            break
print(f"{legendary_item} obtained!")
for material , quantity in materials.items():
    print(f"{material}: {quantity}")