def sort_numbers():
    user_input = input()
    numbers = user_input.split()
    numbers = [int(num) for num in numbers]
    sorted_numbers = sorted(numbers)

    print(sorted_numbers)

sort_numbers()