#Брой пакети химикали - цяло число в интервала [0...100]
#Брой пакети маркери - цяло число в интервала [0...100]
#Литри препарат за почистване на дъска - цяло число в интервала [0…50]
#Процент намаление - цяло число в интервала [0...100]

numb_pck_pen = int(input())
numb_pck_mark = int(input())
liters_detergent = int(input())
discount = int(input())

price_pen = 5.80
price_mark = 7.20
price_per_liter_detergent = 1.20

total_price = (numb_pck_pen * price_pen) + (numb_pck_mark * price_mark) + (liters_detergent * price_per_liter_detergent)
final_discount = total_price * (discount / 100)

final_price = total_price - final_discount

print(final_price)