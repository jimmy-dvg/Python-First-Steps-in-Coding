def absolute_values(numbers_str):
    numbers = numbers_str.split()
    abs_list = [abs(float(num)) for num in numbers]
    return abs_list

data = input()

print(absolute_values(data))