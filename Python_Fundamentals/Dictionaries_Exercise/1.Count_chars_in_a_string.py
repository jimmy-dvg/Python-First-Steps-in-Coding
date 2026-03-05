characters  = input()
occurrences = {}
for character in characters:
    if character == " ":
        continue
    if character not in occurrences.keys():
        occurrences[character] = 0
    occurrences[character] += 1
    # if character not in occurrences.keys():
    #     occurrences[character] = 1
    # else:
    #     occurrences[character] += 1
for character, repetitions in occurrences.items():
    print(f"{character} -> {repetitions}")