remove = input()
text = input()

while remove in text:
    text = text.replace(remove, "")

print(text)