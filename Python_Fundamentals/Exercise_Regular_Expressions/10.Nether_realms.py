import re

raw_input = input().split(',')
demon_names = [name.strip() for name in raw_input if name.strip()]
demon_names.sort()

number_pattern = r'[+-]?\d+(?:\.\d+)?'

health_pattern = r'[^0-9+\-*/.]'

for name in demon_names:
    health_chars = re.findall(health_pattern, name)
    health = sum(ord(char) for char in health_chars)

    numbers = re.findall(number_pattern, name)
    base_damage = sum(float(num) for num in numbers)

    for char in name:
        if char == '*':
            base_damage *= 2
        elif char == '/':
            base_damage /= 2

    print(f"{name} - {health} health, {base_damage:.2f} damage")