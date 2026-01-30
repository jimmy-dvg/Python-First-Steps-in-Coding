divisor = int(input())
boundry = int(input())
for current_number in range(boundry, divisor - 1, -1 ):
    if current_number % divisor == 0:
        break
print(current_number)
