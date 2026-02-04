to_do_list = []

while True:
    entry = input()

    if entry == "End":
        break

    importance, note = entry.split("-", 1)
    importance = int(importance)

    new_item = [importance, note]

    if not to_do_list:
        to_do_list.append(new_item)
        continue

    placed = False

    for i in range(len(to_do_list)):
        if importance < to_do_list[i][0]:
            temp = to_do_list.pop(i)
            to_do_list.insert(i, new_item)
            to_do_list.insert(i + 1, temp)
            placed = True
            break

    if not placed:
        to_do_list.append(new_item)
result = [note for _, note in to_do_list]
print(result)