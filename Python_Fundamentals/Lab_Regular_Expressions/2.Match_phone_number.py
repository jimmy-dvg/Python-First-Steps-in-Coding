import re

text = input()

pattern = r'(?<!\S)\+359([ -])2\1\d{3}\1\d{4}\b'

matches = re.findall(pattern, text)

full_matches = [m.group() for m in re.finditer(pattern, text)]

print(', '.join(full_matches))