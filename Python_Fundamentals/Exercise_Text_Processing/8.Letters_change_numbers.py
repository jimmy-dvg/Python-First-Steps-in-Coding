import sys

tokens = input().split()
total = 0.0

for token in tokens:
    first = token[0]
    last = token[-1]
    middle = token[1:-1]

    # Skip tokens that do not contain a valid number
    if not middle.isdigit():
        continue

    number = int(middle)

    first_pos = ord(first.lower()) - ord('a') + 1
    last_pos = ord(last.lower()) - ord('a') + 1

    # First letter rule
    if first.isupper():
        result = number / first_pos
    else:
        result = number * first_pos

    # Last letter rule
    if last.isupper():
        result -= last_pos
    else:
        result += last_pos

    total += result

print(f"{total:.2f}")