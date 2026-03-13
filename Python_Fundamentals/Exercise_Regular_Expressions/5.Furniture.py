import re

furniture_list = []
total_cost = 0

while True:
    line = input()
    if line == "Purchase":
        break

    pattern = r'>>([\w\s]+)<<(\d+\.?\d*)!(\d+)'
    match = re.match(pattern, line)

    if match:
        name = match.group(1)
        price = float(match.group(2))
        quantity = int(match.group(3))

        furniture_list.append(name)
        total_cost += price * quantity

print("Bought furniture:")
for name in furniture_list:
    print(name)
print(f"Total money spend: {total_cost:.2f}")