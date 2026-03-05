n = int(input())

# Read the field
field = []
for _ in range(n):
    row = list(map(int, input().split()))
    field.append(row)

# Read attacks
attacks = input().split()

destroyed = 0

for attack in attacks:
    r, c = map(int, attack.split("-"))
    if field[r][c] > 0:
        field[r][c] -= 1
        if field[r][c] == 0:
            destroyed += 1

print(destroyed)