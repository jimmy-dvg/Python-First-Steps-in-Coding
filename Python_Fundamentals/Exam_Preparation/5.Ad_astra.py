import re

text = input()

# regex pattern
pattern = r"([#|])([A-Za-z ]+)\1(\d{2}/\d{2}/\d{2})\1(\d+)\1"

matches = re.findall(pattern, text)

total_calories = 0
foods = []

for match in matches:
    item_name = match[1]
    expiration_date = match[2]
    calories = int(match[3])

    total_calories += calories
    foods.append((item_name, expiration_date, calories))

# calculate days
days = total_calories // 2000

print(f"You have food to last you for: {days} days!")

# print each food item
for item in foods:
    print(f"Item: {item[0]}, Best before: {item[1]}, Nutrition: {item[2]}")