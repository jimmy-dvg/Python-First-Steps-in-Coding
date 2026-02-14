energy = float(input())

mountain_count = 0
artifact_pieces = 0

artifact_found = False
exhausted = False

while True:
    terrain = input()

    if terrain == "Journey ends here!":
        break

    if terrain == "mountain":
        energy -= 10
        mountain_count += 1

        if mountain_count % 3 == 0:
            artifact_pieces += 1

    elif terrain == "desert":
        energy -= 15

    elif terrain == "forest":
        energy += 7

    if artifact_pieces == 3:
        artifact_found = True
        break

    if energy <= 0:
        exhausted = True
        break

if artifact_found:
    print(f"The character reached the legendary artifact with {energy:.2f} energy left.")
elif exhausted:
    print("The character is too exhausted to carry on with the journey.")
else:
    needed = 3 - artifact_pieces
    print(f"The character could not find all the pieces and needs {needed} more to complete the legendary artifact.")


