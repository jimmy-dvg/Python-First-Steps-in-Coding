trip_price = float(input())
puzzles = int(input())
dolls = int(input())
bears = int(input())
minions = int(input())
trucks = int(input())

price_puzzle = 2.60
price_doll = 3.00
price_bear = 4.10
price_minion = 8.20
price_truck = 2.00

total_toys = puzzles + dolls + bears + minions + trucks
total_price = (puzzles * price_puzzle +
               dolls * price_doll +
               bears * price_bear +
               minions * price_minion +
               trucks * price_truck)

if total_toys >= 50:
    total_price *= 0.75

total_price *= 0.90

if total_price >= trip_price:
    print(f"Yes! {total_price - trip_price:.2f} lv left.")
else:
    print(f"Not enough money! {trip_price - total_price:.2f} lv needed.")
