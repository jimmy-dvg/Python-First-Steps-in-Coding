def round_numbers(numbers_str):
    numbers = numbers_str.split()
    rounded = [round(float(num)) for num in numbers]
    return rounded

user_input = input()
result = round_numbers(user_input)
print(result)