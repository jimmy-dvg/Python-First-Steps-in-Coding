text = input()

numbers = []
non_numbers = []

# Split into digits and non-digits
for ch in text:
    if ch.isdigit():
        numbers.append(int(ch))
    else:
        non_numbers.append(ch)

# Split into take and skip lists
take_list = numbers[0::2]
skip_list = numbers[1::2]

result = []
index = 0  # current position in non_numbers

# Process take/skip
for take, skip in zip(take_list, skip_list):
    # Take characters
    result.extend(non_numbers[index:index + take])
    index += take  # move forward by taken count
    index += skip  # skip characters

print("".join(result))