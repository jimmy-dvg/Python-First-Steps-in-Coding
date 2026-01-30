text = input()

indices = []
index = 0

for char in text:
    if char.isupper():
        indices.append(index)
    index += 1
print(indices)
