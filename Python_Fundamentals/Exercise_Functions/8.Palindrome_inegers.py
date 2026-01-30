def check_palindromes():
    numbers = input().split(", ")

    for number in numbers:
        if number == number[::-1]:
            print(f"True")
        else:
            print(f"False")


check_palindromes()