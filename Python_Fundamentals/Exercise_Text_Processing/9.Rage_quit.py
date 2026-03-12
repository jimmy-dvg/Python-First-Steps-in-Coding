text = input()
rage_message = ""
sub_string = ""
repetitions = ""

for index in range(len(text)):
    # Case where we have non-numeric symbol
    if not text[index].isdigit():
        sub_string += text[index].upper()
        # Case where we have digit
    else:  # elif text[index].isdigit()
        repetitions += text[index]
        if index + 1 < len(text):
            if text[index + 1].isdigit():
                repetitions += text[index + 1]
        rage_message += sub_string * int(repetitions)
        sub_string = ""
        repetitions = ""

print(f"Unique symbols used: {len(set(rage_message))}")
print(rage_message)