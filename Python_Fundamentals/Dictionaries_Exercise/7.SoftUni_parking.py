n = int(input())
parking = {}

for _ in range(n):
    parts = input().split()
    command = parts[0]
    username = parts[1]

    if command == "register":
        plate = parts[2]
        if username in parking:
            print(f"ERROR: already registered with plate number {parking[username]}")
        else:
            parking[username] = plate
            print(f"{username} registered {plate} successfully")

    elif command == "unregister":
        if username not in parking:
            print(f"ERROR: user {username} not found")
        else:
            parking.pop(username)
            print(f"{username} unregistered successfully")

for user, plate in parking.items():
    print(f"{user} => {plate}")