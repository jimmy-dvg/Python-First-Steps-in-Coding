stops = input()

while True:
    command = input()

    if command == "Travel":
        break

    parts = command.split(":")
    action = parts[0]

    match action:

        case "Add Stop":
            index = int(parts[1])
            string_to_add = parts[2]

            if 0 <= index < len(stops):
                stops = stops[:index] + string_to_add + stops[index:]

        case "Remove Stop":
            start = int(parts[1])
            end = int(parts[2])

            if 0 <= start <= end < len(stops):
                stops = stops[:start] + stops[end + 1:]

        case "Switch":
            old_string = parts[1]
            new_string = parts[2]

            if old_string in stops:
                stops = stops.replace(old_string, new_string)

    print(stops)

print(f"Ready for world tour! Planned stops: {stops}")