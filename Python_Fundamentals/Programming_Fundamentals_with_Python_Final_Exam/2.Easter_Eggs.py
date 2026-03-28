import re

text = input()

pattern = r'[@#]+([a-z]{3,})[@#]+[^a-zA-Z\d]*/+(\d+)/+'

matches = re.finditer(pattern, text)

for match in matches:
    color = match.group(1)
    amount = match.group(2)
    print(f"You found {amount} {color} eggs!")