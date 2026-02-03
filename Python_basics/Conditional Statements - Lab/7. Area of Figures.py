from math import pi

figure = input()
area = 0
if figure == "square":
    side = float(input())
    area = side * side
elif figure == "rectangle":
    length = float(input())
    width = float(input())
    area = length * width
elif figure == "circle":
    radius = float(input())
    area = pi * radius * radius
elif figure == "triangle":
    base = float(input())
    height = float(input())
    area = (base * height) / 2

print(f"{area:.3f}")