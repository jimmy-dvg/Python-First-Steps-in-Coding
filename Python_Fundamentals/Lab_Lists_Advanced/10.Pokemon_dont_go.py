numbers = [int(x) for x in input().split()]
removed_sum = 0

while numbers:
	index = int(input())

	if index < 0:
		first_copy = numbers[-1]
		removed_element = numbers.pop(0)
		numbers.insert(0, first_copy)
	elif index >= len(numbers):
		last_copy = numbers[0]
		removed_element = numbers.pop()
		numbers.append(last_copy)
	else:
		removed_element = numbers.pop(index)

	removed_sum += removed_element

	for i in range(len(numbers)):
		if numbers[i] <= removed_element:
			numbers[i] += removed_element
		else:
			numbers[i] -= removed_element

print(removed_sum)
