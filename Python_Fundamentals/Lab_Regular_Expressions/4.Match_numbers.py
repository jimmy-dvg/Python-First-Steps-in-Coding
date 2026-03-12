import re

text = input()

pattern = r"(?<!\S)-?\d+(\.\d+)?(?!\S)"

matches = re.findall(pattern, text)

numbers = [m.group() for m in re.finditer(pattern, text)]

print(" ".join(numbers))