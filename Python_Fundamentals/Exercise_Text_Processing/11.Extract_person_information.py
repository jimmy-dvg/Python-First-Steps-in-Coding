import re

n = int(input())

for _ in range(n):
    text = input()

    name_match = re.search(r'@([^|]+)\|', text)
    age_match = re.search(r'#([^*]+)\*', text)

    if name_match and age_match:
        name = name_match.group(1)
        age = age_match.group(1)
        print(f"{name} is {age} years old.")