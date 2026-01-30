coffees = 0
valid_event = ["coding", "dog", "cat", "movie"]

while True:
    event = input()
    if event == "END":
        break
    event_lower = event.lower()
    if event_lower in valid_event:
        if event.islower():
            coffees += 1
        elif event.isupper():
            coffees += 2

if coffees > 5:
    print("You need extra sleep")
else:
    print(coffees)