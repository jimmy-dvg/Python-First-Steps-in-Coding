n = int(input())
p = int(input())

mask = 1 << p
mask = ~mask
newNumber = n & mask

print(newNumber)