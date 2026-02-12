def fire(ship_sections: list, current_command: list) -> list and bool:
    index, damage = int(current_command[1]), int(current_command[2])
    if index in range(len(ship_sections)):
        ship_sections[index] -= damage
        if ship_sections[index] <= 0:
            return ship_sections, True
    return ship_sections, False


def defend(ship_sections: list, current_command: list) -> list and bool:
    start_index, end_index, damage = int(current_command[1]), int(current_command[2]), int(current_command[3])
    if start_index in range(len(ship_sections)) and \
            end_index in range(len(ship_sections)):
        for section_index in range(start_index, end_index + 1):
            ship_sections[section_index] -= damage
            if ship_sections[section_index] <= 0:
                return ship_sections, True
    return ship_sections, False


def repair(ship_sections: list, current_command: list, max_health: int) -> list:
    index, health = int(current_command[1]), int(current_command[2])
    if index in range(len(ship_sections)):
        ship_sections[index] += health
        if ship_sections[index] > max_health:
            ship_sections[index] = max_health
    return ship_sections


def status(ship_sections: list, max_health: int) -> str:
    count = len([section for section in ship_sections if section < max_health / 5])
    # count = 0
    # for index in range(len(ship_sections)):
    #     if ship_sections[index] < max_health * 0.2:
    #         count += 1
    return f"{count} sections need repair."


pirate_ship_sections = [int(section) for section in input().split(">")]
war_ship_sections = [int(section) for section in input().split(">")]
maximum_health_per_section = int(input())
war_ship_has_sunken = False
pirate_ship_has_sunken = False
command = input().split()
while "Retire" not in command:
    action = command[0]
    if action == "Fire":
        war_ship_sections, war_ship_has_sunken = fire(war_ship_sections, command)
    elif action == "Defend":
        pirate_ship_sections, pirate_ship_has_sunken = defend(pirate_ship_sections, command)
    elif action == "Repair":
        pirate_ship_sections = repair(pirate_ship_sections, command, maximum_health_per_section)
    elif action == "Status":  # else
        print(status(pirate_ship_sections, maximum_health_per_section))
    if war_ship_has_sunken or pirate_ship_has_sunken:
        break
    command = input().split()
if war_ship_has_sunken:
    print("You won! The enemy ship has sunken.")
elif pirate_ship_has_sunken:
    print("You lost! The pirate ship has sunken.")
else:  # Stalemate
    print(f"Pirate ship status: {sum(pirate_ship_sections)}")
    print(f"Warship status: {sum(war_ship_sections)}")
