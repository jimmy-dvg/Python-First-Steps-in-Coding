import sys

text = sys.stdin.read().strip().split()
result = []

for word in text:
    i = 0
    while i < len(word) and word[i].isdigit():
        i += 1

    ascii_code = int(word[:i])
    first_char = chr(ascii_code)

    rest = list(word[i:])
    if len(rest) > 1:
        rest[0], rest[-1] = rest[-1], rest[0]

    result.append(first_char + "".join(rest))

print(" ".join(result))