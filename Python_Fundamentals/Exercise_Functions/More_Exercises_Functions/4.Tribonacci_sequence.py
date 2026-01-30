def tribonacci():
    n = int(input())

    num1 = 1
    num2 = 1
    num3 = 2

    result = [num1, num2, num3]

    for i in range(n - 3):
        next_num = num1 + num2 + num3
        result.append(next_num)

        num1 = num2
        num2 = num3
        num3 = next_num

    print(' '.join(map(str, result[:n])))


tribonacci()