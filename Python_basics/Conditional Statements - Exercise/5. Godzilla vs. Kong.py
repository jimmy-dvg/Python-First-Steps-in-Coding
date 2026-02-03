movie_budget = float(input())
statists = int(input())
price_for_clothes = float(input())

decor = movie_budget * 0.1

total_price_for_clothes = statists * price_for_clothes

if statists > 150:
    total_price_for_clothes *= 0.90

total_costs = decor + total_price_for_clothes

difference = abs(total_costs - movie_budget)

if total_costs > movie_budget:
    print("Not enough money!")
    print(f"Wingard needs {difference:.2f} leva more.")
elif total_costs <= movie_budget:
    print("Action!")
    print(f"Wingard starts filming with {difference:.2f} leva left.")
