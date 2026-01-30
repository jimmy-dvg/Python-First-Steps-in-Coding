number = int(input())

digits = []

while number > 0:
    digits.append(number % 10)
    number = number // 10

digits.sort(reverse=True)

largest_number = 0
for digit in digits:
    largest_number = largest_number * 10 + digit

print(largest_number)