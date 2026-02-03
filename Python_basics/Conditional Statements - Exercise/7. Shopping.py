budget = float(input())
N = int(input())
M = int(input())
P = int(input())

price_video = N * 250
price_cpu = M * (price_video * 0.35)
price_ram = P * (price_video * 0.10)

total = price_video + price_cpu + price_ram

if N > M:
    total *= 0.85

if budget >= total:
    print(f"You have {budget - total:.2f} leva left!")
else:
    print(f"Not enough money! You need {total - budget:.2f} leva more!")
