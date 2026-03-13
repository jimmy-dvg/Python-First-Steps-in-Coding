import re

links = []

while True:
    try:
        line = input()
        pattern = r'www\.[a-zA-Z0-9-]+(\.[a-z]+)+'
        found = re.findall(pattern, line)
        for match in re.finditer(pattern, line):
            links.append(match.group())
    except EOFError:
        break

for link in links:
    print(link)