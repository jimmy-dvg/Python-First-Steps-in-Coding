def office_happiness():
    happiness_values = list(map(int, input().split()))
    factor = int(input())

    improved = [h * factor for h in happiness_values]

    average = sum(improved) / len(improved)

    happy_count = len([h for h in improved if h >= average])
    total_count = len(improved)

    if happy_count >= total_count / 2:
        print(f"Score: {happy_count}/{total_count}. Employees are happy!")
    else:
        print(f"Score: {happy_count}/{total_count}. Employees are not happy!")


office_happiness()