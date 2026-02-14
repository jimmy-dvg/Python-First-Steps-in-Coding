data = input().split()

while True:
	command = input()

	if command == "3:1":
		break

	parts = command.split()
	action = parts[0]

	if action == "merge":
		start_index = int(parts[1])
		end_index = int(parts[2])

		if start_index < 0:
			start_index = 0
		if end_index >= len(data):
			end_index = len(data) - 1

		if start_index <= end_index and 0 <= start_index < len(data):
			merged = "".join(data[start_index:end_index + 1])
			data[start_index:end_index + 1] = [merged]

	elif action == "divide":
		index = int(parts[1])
		partitions = int(parts[2])

		element = data[index]

		if partitions > 0:
			part_length = len(element) // partitions
			divided = []
			start = 0

			for _ in range(partitions - 1):
				divided.append(element[start:start + part_length])
				start += part_length

			divided.append(element[start:])
			data[index:index + 1] = divided

print(" ".join(data))
