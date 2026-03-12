key = list(map(int, input().split()))

while True:
    line = input()
    if line == "find":
        break

    decrypted = ""

    for i in range(len(line)):
        k = key[i % len(key)]
        decrypted += chr(ord(line[i]) - k)

    start_type = decrypted.index("&") + 1
    end_type = decrypted.index("&", start_type)
    treasure_type = decrypted[start_type:end_type]

    start_coord = decrypted.index("<") + 1
    end_coord = decrypted.index(">")
    coordinates = decrypted[start_coord:end_coord]

    print(f"Found {treasure_type} at {coordinates}")