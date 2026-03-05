phonebook = {}
while True:
    entry = input()
    if "-" not in entry:
        break
    name, number = entry.split("-")
    phonebook[name] = number
number_of_searches = int(entry)
for search in range(number_of_searches):
    searched_name = input()
    if searched_name in phonebook.keys():
        number = phonebook[searched_name]
        print(f"{searched_name} -> {number}")
    else:
        print(f"Contact {searched_name} does not exist.")