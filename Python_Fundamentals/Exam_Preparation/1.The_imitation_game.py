message = input()

while True:
    command = input()

    if command == "Decode":
        break

    parts = command.split("|")
    action = parts[0]

    if action == "Move":
        n = int(parts[1])
        # move first n letters to the end
        message = message[n:] + message[:n]

    elif action == "Insert":
        index = int(parts[1])
        value = parts[2]
        # insert value before index
        message = message[:index] + value + message[index:]

    elif action == "ChangeAll":
        substring = parts[1]
        replacement = parts[2]
        # replace all occurrences
        message = message.replace(substring, replacement)

print(f"The decrypted message is: {message}")