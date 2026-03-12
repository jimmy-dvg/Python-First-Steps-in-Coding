text = input()
encrypted_text = ""
for character in text:
    encrypted_symbol = chr(ord(character) + 3)
    encrypted_text += encrypted_symbol
print(encrypted_text)