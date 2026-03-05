population = list(map(int, input().split(", ")))
min_wealth = int(input())

total_wealth = sum(population)
needed_wealth = min_wealth * len(population)

if total_wealth < needed_wealth:
    print("No equal distribution possible")
else:
    # Iterate through each person
    for i in range(len(population)):
        if population[i] < min_wealth:
            # Calculate how much this person needs
            needed = min_wealth - population[i]

            # Find the current richest person to take from
            richest_index = population.index(max(population))

            # Transfer the wealth
            population[richest_index] -= needed
            population[i] += needed

    print(population)