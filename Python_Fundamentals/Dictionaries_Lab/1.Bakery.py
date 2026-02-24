line = input().split()
stock = {}

for i in range(0, len(line), 2):
    stock[line[i]] = int(line[i + 1])

print(stock)