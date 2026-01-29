nylon = int(input())
paint = int(input())
thinner = int(input())
hours = int(input())

nylon_price = 1.50
paint_price = 14.50
thinner_price = 5.00
bags_price = 0.40

nylon_total = nylon + 2
paint_total = paint * 1.10

materials_cost = nylon_total * nylon_price + paint_total * paint_price + thinner * thinner_price + bags_price

workers_cost = materials_cost * 0.30 * hours

total = materials_cost + workers_cost

print(total)