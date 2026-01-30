def check_sign():
    num1 = int(input())
    num2 = int(input())
    num3 = int(input())

    negative_count = 0

    if num1 < 0:
        negative_count += 1
    if num2 < 0:
        negative_count += 1
    if num3 < 0:
        negative_count += 1

    if num1 == 0 or num2 == 0 or num3 == 0:
        print("zero")

    elif negative_count % 2 == 1:
        print("negative")
    else:
        print("positive")


check_sign()