morse_code = input().split(" | ")

morse_dict = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D",
    ".": "E", "..-.": "F", "--.": "G", "....": "H",
    "..": "I", ".---": "J", "-.-": "K", ".-..": "L",
    "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T",
    "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z"
}

result = []

for word in morse_code:
    letters = word.split()
    decoded_word = ""

    for letter in letters:
        decoded_word += morse_dict[letter]

    result.append(decoded_word)

print(" ".join(result))