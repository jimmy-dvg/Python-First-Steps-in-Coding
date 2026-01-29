chicken_menus = int(input())
fish_menus = int(input())
veggie_menus = int(input())

chicken_price = 10.35
fish_price = 12.40
veggie_price = 8.15

total_food = chicken_menus * chicken_price + fish_menus * fish_price + veggie_menus * veggie_price

dessert = total_food * 0.20

delivery = 2.50

total = total_food + dessert + delivery

print(f"{total:.2f}")
