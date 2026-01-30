def rectangle_area(width, height):
    return width * height

w = float(input())
h = float(input())

area = rectangle_area(w, h)
print(round(area))