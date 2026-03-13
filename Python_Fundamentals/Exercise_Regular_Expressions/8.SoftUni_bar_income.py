import re


pattern = r'%([A-Z][a-z]+)%[^%|$.]*<(\w+)>[^%|$.]*\|(\d+)\|[^%|$.]*?(\d+(?:\.\d+)?)\$'

total_income = 0

while True:
    line = input()

    if line == "end of shift":
        break

    matches = re.finditer(pattern, line)

    for match in matches:
        customer = match.group(1)
        product = match.group(2)
        count = int(match.group(3))
        price = float(match.group(4))

        total_price = count * price
        total_income += total_price

        print(f"{customer}: {product} - {total_price:.2f}")

print(f"Total income: {total_income:.2f}")