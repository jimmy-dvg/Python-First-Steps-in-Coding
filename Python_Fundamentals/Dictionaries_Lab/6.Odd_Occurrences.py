words = input().split()
counts = {}

for word in words:
    lower = word.lower()
    if lower in counts:
        counts[lower] += 1
    else:
        counts[lower] = 1

result = []
seen = set()

for word in words:
    lower = word.lower()
    if counts[lower] % 2 != 0 and lower not in seen:
        result.append(lower)
        seen.add(lower)

print(" ".join(result))