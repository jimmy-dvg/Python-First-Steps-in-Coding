n = int(input())
b = int(input())

binary = bin(n)[2:]
count = binary.count(str(b))

print(count)