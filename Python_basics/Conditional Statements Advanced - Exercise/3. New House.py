flower_type = input()
number_of_flowers = int(input())
budget = int(input())
price = 0

#"Roses", "Dahlias", "Tulips", "Narcissus" или "Gladiolus"

if flower_type == "Roses":
    price = 5 * number_of_flowers
    if number_of_flowers > 80:
        price *= 0.90
elif flower_type == "Dahlias":
    price = 3.80 * number_of_flowers
    if number_of_flowers > 90:
        price *= 0.85
elif flower_type == "Tulips":
    price = 2.80 * number_of_flowers
    if number_of_flowers > 80:
        price *= 0.85
elif flower_type == "Narcissus":
    price = 3 * number_of_flowers
    if number_of_flowers < 120:
        price += price * 0.15
elif flower_type == "Gladiolus":
    price = 2.50 * number_of_flowers
    if number_of_flowers < 80:
        price += price * 0.20

difference = abs(budget-price)

if budget >= price:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {difference:.2f} leva left.")
else:
    print(f"Not enough money, you need {difference:.2f} leva more.")