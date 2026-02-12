def merge_elements(data, start, end):
    # Clamp indices
    start = max(0, start)
    end = min(len(data) - 1, end)

    if start > end:
        return data

    merged = "".join(data[start:end + 1])

    return data[:start] + [merged] + data[end + 1:]


def divide_element(data, index, partitions):
    element = data[index]
    length = len(element)

    part_size = length // partitions
    remainder = length % partitions

    new_parts = []
    start = 0

    for i in range(partitions):
        extra = 1 if i < remainder else 0
        end = start + part_size + extra
        new_parts.append(element[start:end])
        start = end

    return data[:index] + new_parts + data[index + 1:]


def main():
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
            data = merge_elements(data, start_index, end_index)

        elif action == "divide":
            index = int(parts[1])
            partitions = int(parts[2])
            data = divide_element(data, index, partitions)

    print(" ".join(data))


if __name__ == "__main__":
    main()