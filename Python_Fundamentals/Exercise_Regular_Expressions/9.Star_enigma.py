import re

n = int(input())
attacked_planets = []
destroyed_planets = []

pattern = r'@([A-Za-z]+)[^@\-!:>]*:(\d+)[^@\-!:>]*!([AD])![^@\-!:>]*->(\d+)'

for _ in range(n):
    encrypted_message = input()
    lower_message = encrypted_message.lower()
    key = lower_message.count('s') + lower_message.count('t') + \
          lower_message.count('a') + lower_message.count('r')

    decrypted_message = ""
    for char in encrypted_message:
        decrypted_message += chr(ord(char) - key)

    match = re.search(pattern, decrypted_message)

    if match:
        planet_name = match.group(1)
        attack_type = match.group(3)

        if attack_type == 'A':
            attacked_planets.append(planet_name)
        elif attack_type == 'D':
            destroyed_planets.append(planet_name)

print(f"Attacked planets: {len(attacked_planets)}")
for planet in sorted(attacked_planets):
    print(f"-> {planet}")

print(f"Destroyed planets: {len(destroyed_planets)}")
for planet in sorted(destroyed_planets):
    print(f"-> {planet}")