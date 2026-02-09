def memory_game():
    elements = input().split()
    moves = 0

    while True:
        command = input()

        if command == "end":
            break

        indexes = command.split()
        index1 = int(indexes[0])
        index2 = int(indexes[1])

        moves += 1

        if index1 == index2 or index1 < 0 or index1 >= len(elements) or index2 < 0 or index2 >= len(elements):
            new_element = f"-{moves}a"
            middle = len(elements) // 2
            elements.insert(middle, new_element)
            elements.insert(middle, new_element)
            print("Invalid input! Adding additional elements to the board")
        else:
            if elements[index1] == elements[index2]:
                element = elements[index1]
                print(f"Congrats! You have found matching elements - {element}!")

                if index1 > index2:
                    elements.pop(index1)
                    elements.pop(index2)
                else:
                    elements.pop(index2)
                    elements.pop(index1)

                if len(elements) == 0:
                    print(f"You have won in {moves} turns!")
                    return
            else:
                print("Try again!")

    print("Sorry you lose :(")
    print(' '.join(elements))

memory_game()