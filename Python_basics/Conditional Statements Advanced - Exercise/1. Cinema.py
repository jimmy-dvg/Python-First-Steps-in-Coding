projection_type = input()
rows = int(input())
columns = int(input())

total_seats = rows * columns
price = 0

if projection_type == "Premiere":
    price = 12
elif projection_type == "Normal":
    price = 7.50
elif projection_type == "Discount":
    price = 5

total_income = total_seats * price

print(f"{total_income:.2f} leva")
