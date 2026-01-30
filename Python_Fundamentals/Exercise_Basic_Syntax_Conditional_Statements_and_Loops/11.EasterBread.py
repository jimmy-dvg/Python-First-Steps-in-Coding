budget = float(input())
flour_price = float(input())

eggs_price = 0.75 * flour_price
milk_price_per_liter = 1.25 * flour_price
milk_cost = 0.25 * milk_price_per_liter

cost_per_bread = eggs_price + flour_price + milk_cost

loaves = 0
eggs_collected = 0

while budget >= cost_per_bread:
    budget -= cost_per_bread
    loaves += 1
    eggs_collected += 3

    if loaves % 3 == 0:
        eggs_collected -= (loaves - 2)

print(f"You made {loaves} loaves of Easter bread! Now you have {eggs_collected} eggs and {budget:.2f}BGN left.")
