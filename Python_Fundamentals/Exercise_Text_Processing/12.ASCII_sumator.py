start_char = input()
end_char = input()
text = input()

start_ascii = ord(start_char)
end_ascii = ord(end_char)

total = 0

for ch in text:
    if start_ascii < ord(ch) < end_ascii:
        total += ord(ch)

print(total)