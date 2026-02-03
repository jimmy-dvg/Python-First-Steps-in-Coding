days = int(input())
room_type = input()
rating = input()

nights = days - 1
price = 0

if room_type == "room for one person":
    price = nights * 18
elif room_type == "apartment":
    price = nights * 25
    if nights < 10:
        price *= 0.70
    elif nights <= 15:
        price *= 0.65
    else:
        price *= 0.50
elif room_type == "president apartment":
    price = nights * 35
    if nights < 10:
        price *= 0.90
    elif nights <= 15:
        price *= 0.85
    else:
        price *= 0.80

if rating == "positive":
    price *= 1.25
else:
    price *= 0.90

print(f"{price:.2f}")
