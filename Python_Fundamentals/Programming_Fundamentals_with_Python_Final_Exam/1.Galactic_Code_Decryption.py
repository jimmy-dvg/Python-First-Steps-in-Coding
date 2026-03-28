message = input()

while True:
    command = input()

    if command == "Finalize":
        break

    elif command == "Encrypt":
        message = message[::-1]
        print(message)

    elif command == "Decrypt":
        new_message = ""
        for char in message:
            if char.isupper():
                new_message += char.lower()
            elif char.islower():
                new_message += char.upper()
            else:
                new_message += char
        message = new_message
        print(message)

    elif command.startswith("Substitute"):
        parts = command.split(" ")
        old_char = parts[1]
        new_char = parts[2]
        if old_char not in message:
            print("Character not found.")
        else:
            message = message.replace(old_char, new_char)
            print(message)

    elif command.startswith("Scramble"):
        parts = command.split(" ")
        index = int(parts[1])
        char = parts[2]
        if index < 0 or index >= len(message):
            print("Index out of bounds.")
        else:
            message = message[:index] + char + message[index + 1:]
            print(message)

    elif command.startswith("Remove"):
        parts = command.split(" ", 1)
        substring = parts[1]
        message = message.replace(substring, "")
        print(message)

    else:
        print("Invalid command detected!")