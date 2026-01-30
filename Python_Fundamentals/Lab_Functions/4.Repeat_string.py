def repeat_string(text, n):
    repeat = lambda t, count: t * count
    return repeat(text, n)


string_input = input()
counter = int(input())

print(repeat_string(string_input, counter))