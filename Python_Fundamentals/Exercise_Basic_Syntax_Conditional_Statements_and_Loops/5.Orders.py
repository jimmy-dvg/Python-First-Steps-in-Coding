n = int(input())
total_price = 0.0

for _ in range(n):
    price_per_capsule = float(input())
    days = int(input())
    capsules_per_day = int(input())

    if not (0.01 <= price_per_capsule <= 100.00):
        continue
    if not (1 <= days <= 31):
        continue
    if not (1 <= capsules_per_day <= 2000):
        continue

    order_price = price_per_capsule * days * capsules_per_day
    total_price += order_price

    print(f"The price for the coffee is: ${order_price:.2f}")

print(f"Total: ${total_price:.2f}")