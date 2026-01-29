tax = int(input())

shoes = tax * 0.6
clothes = shoes * 0.8
ball = clothes / 4
accessories = ball / 5

total = tax + shoes + clothes + ball + accessories

print(f"{total:.2f}")
