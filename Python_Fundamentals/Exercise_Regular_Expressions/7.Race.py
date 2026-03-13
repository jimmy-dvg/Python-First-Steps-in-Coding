import re

participants = input().split(", ")
distances = {}

while True:
    line = input()
    if line == "end of race":
        break

    letters = ''.join(re.findall(r'[a-zA-Z]', line))
    digits = re.findall(r'\d', line)
    distance = sum(int(d) for d in digits)

    if letters in participants:
        if letters in distances:
            distances[letters] += distance
        else:
            distances[letters] = distance

top3 = sorted(distances, key=lambda x: distances[x], reverse=True)[:3]

places = ["1st", "2nd", "3rd"]
for i, racer in enumerate(top3):
    print(f"{places[i]} place: {racer}")