grid = [int(x) for x in input().split("|")]
total_collected = 0

while True:
	command = input()

	if command == "Adventure over":
		break

	if command.startswith("Step Backward$"):
		_, start_index_str, steps_str = command.split("$")
		start_index = int(start_index_str)
		steps = int(steps_str)

		if 0 <= start_index < len(grid):
			landing_index = (start_index - steps) % len(grid)
			total_collected += grid[landing_index]
			grid[landing_index] = 0

	elif command.startswith("Step Forward$"):
		_, start_index_str, steps_str = command.split("$")
		start_index = int(start_index_str)
		steps = int(steps_str)

		if 0 <= start_index < len(grid):
			landing_index = (start_index + steps) % len(grid)
			total_collected += grid[landing_index]
			grid[landing_index] = 0

	elif command.startswith("Double "):
		index = int(command.split()[1])
		if 0 <= index < len(grid):
			grid[index] *= 2

	elif command == "Switch":
		grid.reverse()

print(" - ".join(str(x) for x in grid))
print(f"Robo finished the adventure with {total_collected} items!")
